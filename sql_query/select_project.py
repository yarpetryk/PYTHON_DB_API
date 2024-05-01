
class SQLQuery:
    def __init__(self, conn):
        self.conn = conn

    def select_project(self, project_details='%doors%',  project_status='done'):
        selected_projects = []
        cursor = self.conn.cursor()
        cursor.execute("""
                SELECT * FROM Tasks
                WHERE details LIKE ? AND status = ? """, [project_details, project_status])
        columns = [description[0] for description in cursor.description]
        print(columns)

        result = cursor.fetchall()
        for row in result:
            selected_projects.append(row['project'])
            print('Id:        ', row['id'])
            print('Priority:  ', row['priority'])
            print('Details:   ', row['details'])
            print('Status:    ', row['status'])
            print('Completed: ', row['completed'])
            print('Deadline:  ', row['deadline'])
            print('Project:   ', row['project'])
            print('\n')

        self.conn.close()
        print(selected_projects)
        return selected_projects
