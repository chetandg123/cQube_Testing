from HTMLTestRunner import HTMLTestRunner
import unittest

from Sanity_Testing.Test_Scripts import Check_Cluster_records, Choose_District_count_Dots, Click_on_Blocks_Button, \
    Click_on_Blocks_Check_Records, Click_on_Clusters, Click_on_CRCreport, Click_on_Dash_menu, Click_on_District_Block, \
    Click_on_Download_icon, Click_on_Home_icon, Click_on_Schools_Btn, Click_on_Semester, Click_on_TAR, \
    Cluster_wise_Details, Invalid_credentials_check, Login_and_logout, login_with_invalid_credentials, \
    login_with_invalid_password, login_to_cQube, login_with_invalid_user, login_with_unuser, login_with_wrong_user, \
    login_with_wrong_user_password, login_wrong_credentials, Schools_details, Url_test, Login_Negative_test, \
    login_test_with_invalid_user, Click_on_CRC_Districts

from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Sanity_test = unittest.TestSuite()
        Sanity_test.addTests([
             # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Check_Cluster_records.Test_Distbllk),
            unittest.defaultTestLoader.loadTestsFromTestCase(Choose_District_count_Dots.Dist_choose),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Blocks_Button.Blockbtn_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Blocks_Check_Records.test_blockdetails),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Clusters.test_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_CRCreport.test_crc),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Dash_menu.test_Dashboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_District_Block.Test_Distbllk),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Download_icon.test_download),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Home_icon.test_homeicon),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Schools_Btn.school_btn),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Semester.test_SR),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_TAR.test_TAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_wise_Details.test_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Invalid_credentials_check.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login_and_logout.test_logout),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login_Negative_test.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_test_with_invalid_user.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_to_cQube.Login_to_cQube),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_invalid_credentials.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_invalid_password.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_invalid_user.Login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_unuser.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_wrong_user.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_with_wrong_user_password.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_wrong_credentials.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_details.school_details),
            unittest.defaultTestLoader.loadTestsFromTestCase(Url_test.url_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_CRC_Districts.test_crc_District),
        ])
        p = pwd()
        outfile = open(p.get_sanity_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Sanity Test Result '

        )

        runner1.run(Sanity_test)

if __name__ == '__main__':
    unittest.main()