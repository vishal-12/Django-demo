
def template(data,username):
    email_data = "               ReadMe File \n\n" \
                     "1.File Type : {} \n\n" \
                     "2.Managed Care Plan : {}\n\n" \
                     "3.Performance Year : {}\n\n" \
                     "4.Quarter or Annual Identifier : {}\n\n" \
                     "5.Known data quality issues : {}\n\n" \
                     "6.ChangestotheFileinthisDelivery : {}\n\n" \
                     "7.Upcoming changes approved by ODM : {}\n\n" \
                     "8.User Name : {}".format(
            data.get("FileType"),
            data.get("ManagedCarePlan"),
            data.get("PerformanceYear"),
            data.get("QuarterOrAnualIdentifier"),
            data.get("KnownData"),
            data.get("ChangestotheFileinthisDelivery"),
            data.get("UpcomingChanges"),
            username)
    attachment = "Hi,\n\n" \
                     "Please find attached readme file.\n\n" \
                     "Regards,\n" \
                     "Narender bhukya"

    if data.get("QuarterOrAnnualIdentifier")=='Annual':
        quarter='Q4'
    else:
        quarter=data.get("QuarterOrAnnualIdentifier")
    quarter_filename=str(data.get("PerformanceYear"))+'_'+str(quarter)+'_'+str(data.get("ManagedCarePlan"))

    File_name = None
    if data.get("FileType") == 'File_R MCP_Quarterly_Enrollment_File':
        File_name='Readme_CPC_Medicaid_Managed_Care_Plan_Quarterly_Enrollment_File_'+quarter_filename+'.doc'
    elif data.get("FileType") == 'File_R Revised MCP_Quarterly_Enrollment_File for Add/Del':
        File_name='Readme_CPC_Medicaid_Managed_Care_Plan_Quarterly_Enrollment_File_'+quarter_filename+'_v00.doc'
    elif data.get("FileType") == 'File_D  MCP_payment_and_attribution_validation File for CPC':
        File_name='Readme_D_MCP_payment_and_attribution_validation_'+quarter_filename+'.doc'
    elif data.get("FileType") == 'File_J  CPC Practice Summary Report/ CPC Partnership Summary Report File':
        File_name='Readme.V005.SUMM.ACR.'+'.doc'
    elif data.get("FileType") == 'File_O CPC Member-level provider report CSV data file for MCPs':
        File_name='Readme.V005.DETL.ACR.'+'.doc'
    elif data.get("FileType") == 'File_G5 CPC Shared savings payment file for MCPs':
        File_name='Readme.V005.CPC.ACPR.'+'.doc'

    return email_data,File_name,attachment
