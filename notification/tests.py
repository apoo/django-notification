from django.test import TestCase
from django.contrib.auth import get_user_model

from notification.models import NoticeSetting,NoticeType



class NoticeSettingTest(TestCase):

    def setUp(self):
        """
        Initial Setup for the unit test
        """
        self.user = get_user_model()()
        self.user.username = "blaah"
        self.user.email = "blaah@example.com"
        self.user.set_password("blaah")
        self.user.save()

        self.notice_type_1 = NoticeType(
            label = "meeh",
            display = "meeh",
            description = "Meeh Meeh",
            default = 0,
        )
        self.notice_type_1.save()

        self.notice_type_2 = NoticeType(
            label = "daaa",
            display = "daaa",
            description = "Daaaa Daaaa",
            default = 1,
        )
        self.notice_type_2.save()


    def test_setting_default_notice_settings_for_a_user(self):
        """
        Test class method for saving default settings for a user.
        """

        NoticeSetting.set_user_default_notice_settings(self.user,0)
        obj_from_db_for_user = NoticeSetting.objects.filter(user = self.user)
        self.assertEqual(len(obj_from_db_for_user),2)

    def test_setting_default_notice_settings_correct_notices(self):
        """
        Test class method for saving default settings for a user. Make sure right
        notices have been saved.
        """

        NoticeSetting.set_user_default_notice_settings(self.user,0)
        obj_from_db_for_user = NoticeSetting.objects.filter(user = self.user).order_by('id')

        for notice_setting in obj_from_db_for_user:

            self.assertEqual(notice_setting.user,self.user)
            self.assertEqual(notice_setting.send,True)





