from HTMLTestRunner import HTMLTestRunner
import unittest

from Sanity_Testing.Test_Scripts import Schools_details
from System_Test.Test_scripts import blockdata_check, blocks_csv_download, Check_district_block, \
    click_on_cqube_login, click_logout, click_on_usercreate, user_data_create, click_on_homeButton, cluster_data_check, \
    clusters_csv_download, Home_map, Click_on_school_csv_download, Click_on_block_cluster_schools, click_on_blocks, \
    click_on_cluster, click_on_district, click_on_schools, Click_on_SR_HomeBtn, Cluster_level_dots, \
    Cluster_to_Dashboard, Dashboard_menu, District_clusters, Click_on_Semester, Check_Cluster_records, \
    Choose_District_count_Dots, Click_on_Blocks_Button, Click_on_Blocks_Check_Records, Click_on_Clusters, \
    Click_on_CRCreport, Click_on_Dash_menu, Click_on_District_Block, Click_on_Download_icon, Click_on_Home_icon, \
    Click_on_Schools_Btn, Click_on_TAR, Cluster_wise_Details, Invalid_credentials_check, Login_and_logout, \
    Login_Negative_test, login_test_with_invalid_user, login_to_cQube, login_with_invalid_credentials, \
    login_with_invalid_password, login_with_invalid_user, login_with_unuser, login_with_wrong_user, \
    login_with_wrong_user_password, login_wrong_credentials, Url_test, Click_on_CRC_Districts
from TS import Blocks_random

from get_dir import pwd


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        system_test = unittest.TestSuite()
        system_test.addTests([


            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_block_cluster_schools.SAROption),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_blocks.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_cluster.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_district.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_schools.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_SR_HomeBtn.Home_click),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_level_dots.test_dot_records),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_to_Dashboard.Dashobard_click),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dashboard_menu.Dash_menu),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_clusters.test_cluster),

            unittest.defaultTestLoader.loadTestsFromTestCase(blockdata_check.Blockdata_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(blocks_csv_download.Block_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Blocks_random.District_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Check_district_block.block_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_cqube_login.CqubeLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_logout.SAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_Semester.test_SR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_usercreate.Click_create),
            unittest.defaultTestLoader.loadTestsFromTestCase(user_data_create.user_data),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_homeButton.SAR),

            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_data_check.dist_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(clusters_csv_download.Block_validation),
            unittest.defaultTestLoader.loadTestsFromTestCase(Home_map.Sel_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_school_csv_download.Block_validation),

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
        outfile = open(p.get_system_report_path(), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity=1,
            description='System Test Result '

        )

        runner1.run(system_test)

if __name__ == '__main__':
    unittest.main()