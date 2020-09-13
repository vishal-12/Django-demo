import vertica_python
from readme_service.config import *

def insert_to_db(fileType=None,Managed_care_plan=None,performanceYears=None,quarterOrAnnualIdentifiers=None,
knownDataQualityIssues=None,ChangestotheFileinthisDelivery=None,upcomingChangesApprovedByODM=None,userName=None):
    try:
        cursor = vertica_python.connect(**conn_info)
        cursor= cursor.cursor()
        print ("Database connected...")
        cursor.execute(f"INSERT INTO Presentation_Layer.Readme_files VALUES ('{fileType}','{Managed_care_plan}','{performanceYears}','{quarterOrAnnualIdentifiers}','{knownDataQualityIssues}','{ChangestotheFileinthisDelivery}','{upcomingChangesApprovedByODM}','{userName}');")
        cursor.execute("commit")
        print('Insert Completed!')
    except Exception as e:
        print('Exception in DB Update!' , e)
    finally:
        cursor.close()
        print("Database Connection Closed!")