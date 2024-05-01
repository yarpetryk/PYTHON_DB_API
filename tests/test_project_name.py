import allure
import os
import pytest
from sql_query.select_project import SQLQuery


class TestSQLQuery:

    @allure.step('And test DB')
    @pytest.mark.select_project
    def test_project_name(self, connection):
        project_name = 'first'
        response = SQLQuery(connection)
        assert project_name in response.select_project()
        print(f"The project '{project_name}' is present...")

        for key, val in os.environ.items():
            print(f"{key} = {val}")
        #print(os.environ)
        print(os.environ.get('USERNAME'))
        print(os.getenv('USERNAME'))
        os.environ['USERNAME'] = 'ypetryk'      # set value
        print(os.getenv('USERNAME'))            # get value

