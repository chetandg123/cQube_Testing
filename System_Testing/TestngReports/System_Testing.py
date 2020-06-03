from HTMLTestRunner import HTMLTestRunner
import unittest

from Integration_Testing.Test_scripts import Block_cluster, Change_password_Page, Click_on_block_cluster_schools, \
    click_on_blocks, click_on_cluster, click_on_district, click_on_schools, Cluster_level_dots, Cluster_to_Dashboard, \
    Dashboard_menu, District_clusters, Goto_HomePage_mouseover_on_dots, Graph_xaxis_dropdown, Graph_XY, Graph_Yaxis, \
    map_cluster, Map_validation1, map_validation2, School_records_test, schools_csv_download, Select_District_validate, \
    Select_Type, Set_up_new_password, Click_on_SR_HomeBtn
from Sanity_Testing.Test_Scripts import Check_Cluster_records, Choose_District_count_Dots, Click_on_Blocks_Button, \
    Click_on_Blocks_Check_Records, Click_on_Clusters, Click_on_CRCreport, Click_on_Dash_menu, Click_on_District_Block, \
    Click_on_Download_icon, Click_on_Home_icon, Click_on_Schools_Btn, Click_on_Semester, Click_on_TAR, \
    Cluster_wise_Details, Invalid_credentials_check, Login_and_logout, login_with_invalid_credentials, \
    login_with_invalid_password, login_to_cQube, login_with_invalid_user, login_with_unuser, login_with_wrong_user, \
    login_with_wrong_user_password, login_wrong_credentials, Schools_details, Url_test, Login_Negative_test, \
    login_test_with_invalid_user
from System_Testing.Test_scripts import blockdata_check, blocks_csv_download, Blocks_random, Check_district_block, \
    click_on_cqube_login, click_logout, click_on_usercreate, user_data_create, click_on_homeButton, cluster_data_check, \
    clusters_csv_download, Home_map, Click_on_school_csv_download
from System_Testing.Test_scripts.Fillup_user import Fillup_user
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




        ])
        p = pwd()
        outfile = open(p.get_system_report_path(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='System Test Result '

        )

        runner1.run(system_test)

if __name__ == '__main__':
    unittest.main()