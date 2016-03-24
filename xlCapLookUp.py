import xlwings as xw
import sqlite3

#get crane info from excel sheet
def capLookUp():
    #call workbook and get info from workbook
    wb =xw.Workbook.caller()
    #get values from workbook when crane is in luffing configuration
    if xw.Range('Boom_Config').value == 'SW':
        crane = xw.Range('Name').value
        BoomType = xw.Range('Boom_Config').value
        cwt = xw.Range('CWT').value
        Outrigger = xw.Range('Outrigger').value
        BoomLen = xw.Range('Main_Len').value
        BoomAngle = xw.Range('Jib_Len').value
        JibLen = xw.Range('Jib_Angle').value
        JibAngle = None
    #get values from workbook when crane is in any configuration besides luffing
    else:
        crane = xw.Range('Name').value
        BoomType = xw.Range('Boom_Config').value
        cwt = xw.Range('CWT').value
        Outrigger = xw.Range('Outrigger').value
        BoomLen = xw.Range('Main_Len').value
        BoomAngle = None
        JibLen = xw.Range('Jib_Len').value
        JibAngle = xw.Range('Jib_Angle').value

    def queryDb(crane,dbin):           
    #query db for capacities
        conn = sqlite3.connect('E:\\WinPython-64bit-3.4.3.5\\notebooks\\CraneCapacityLookUp\\crane.db')
        c = conn.cursor()
        c.execute("SELECT Capacity FROM %s WHERE BoomType == ? and Counterweight == ? and Outrigger == ? and BoomLen == ? and BoomAngle == ? or BoomAngle is NULL and JibLen == ? or JibLen is NULL and JibAngle == ? or JibAngle is NULL and Radius >= ?" %crane, dbin)
        Capacity = c.fetchone()
        conn.close()
        return Capacity        
        
    #write capacities to excel sheet
    colRad = 14
    colCap = 12
    row = 11
    while xw.Range((row,colRad)).value != None:
        radius = xw.Range((row,colRad)).value
        dbin = (BoomType,cwt,Outrigger,BoomLen,BoomAngle,JibLen,JibAngle,radius)
        Capacity = queryDb(crane,dbin)
        xw.Range((row,colCap)).value = Capacity
        row = row + 1