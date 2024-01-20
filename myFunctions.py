def CreateSQLTable(tbl_name,df_name):
    i_type = ""
    lst_hdr = 'CREATE TABLE adi.' + srctbl + ' ( tblKey INT IDENTITY(1,1) NOT NULL PRIMARY KEY,'
    lst_ftr = '''CreateDate datetime DEFAULT getdate() NOT NULL, CreateBy varchar(50) default suser_sname() NOT NULL
        ,LastUpdatedDate datetime DEFAULT getdate() NOT NULL, LastUpdatedBy varchar(50) default suser_sname()
        ,LoadDate date NOT NULL, DataDate date NOT NULL, SrcFileName varchar(100) NOT NULL)
        '''
    lst_col = [col for col in df_name]       
    with open(dstfolder + 'sql_Create Table ' + srctbl + '.txt', 'w') as f:
        print(lst_hdr, file=f) 
        for i in lst_col:
            i_type = 'def'
            x3 = i[-3::]
            x2 = i[-2::]
            if x3 == 'DSC' or x2 == 'NM':
                i_type = ' varchar(150),'
            elif x3 == 'DTS':
                i_type = ' datetime,'
            elif x3 == 'NBR' or x3 == 'CNT':
                i_type = ' float,'
            elif x2 == 'CD' or x2 == 'ID':
                i_type = ' varchar(30),'
            elif x3 == 'SEQ':
                i_type = ' int,'
            else:    
                i_type = ' varchar(50),'           
            print(i + i_type, file=f)
        print(lst_ftr, file=f)
