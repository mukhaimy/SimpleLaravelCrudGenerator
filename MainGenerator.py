import os 
from datetime import datetime


class MyLaravelGenerator:
    
    def __init__(self):
        tnow = datetime.now()
        self.strNow = str(tnow.year) + '_' + str(tnow.month).zfill(2) + '_' + \
                    str(tnow.day).zfill(2) + '_' +  str(tnow.hour).zfill(2) + \
                    str(tnow.minute).zfill(2) + str(tnow.second).zfill(2) + '_'

        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        ## PERHATIKAN INI
        self.tableName = 'Demo'
        self.lowerTableName = 'demo'
        self.tablenameVar = 'demo'
        self.delField = 'nama'
        
        self.fdict = {
            '_lowertablename_': self.lowerTableName,
            '_tablename_': self.tableName,
            '_tablenameVar_': self.tablenameVar, 
            '_delField_': self.delField
        }
        self.lfdict = list(self.fdict.keys())
        ## ------

        self.working_dir = self.strNow +  self.tableName
    
        # tipe Field  .., tambahkan sesuai keperluan
        tpString = 'string'
        tpInteger = 'integer'
        tpBigInteger = 'bigInteger'
        tpDate = 'date'
        tpDecimal = 'decimal'
        tpDouble = 'double'
        tpBoolean = 'boolean'
    
        ## PERHATIKAN INI
        self.tableFields = [[tpString, 'nama'],
                      [tpString, 'telpon'],                      
                      ]
        ## ------
    
        
        # Buat Folder untuk distribusi file
        # -----------------------------------
        if not os.path.isdir(self.working_dir):
            os.mkdir(os.path.join(self.dir_path, self.working_dir))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'database'))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'database', 'migrations' ))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'database', 'seeders' ))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'app'))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'app', 'Http'))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'app', 'Http', 'Controllers'))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'app', 'Models'))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'resources'))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'resources', 'views'))
            os.mkdir(os.path.join(self.dir_path, self.working_dir, 'resources', 'views', self.tableName ))
    # --- END of: constructor
        
    
    # **********************************
    # Buat File Migrasi
    # **********************************
    def BuatFileMigrasi(self):        
        text_file_name = os.path.join(self.dir_path, 'b_migration.php')    
        print('read: ', text_file_name)
        text_file = open(text_file_name, 'r')
        data_file = text_file.read()

        # ubah setiap variabel
        for lf in self.lfdict :
            # print(fdict[lf])
            data_file = data_file.replace(lf, self.fdict[lf])
    
        # ubah bagian yang di Loop1
        loop1 = ""
        for item in self.tableFields:
            loop1 += '            $table->' + item[0] + "('" + item[1] + "'); \n"
        
        data_file = data_file.replace('_Loop1_', loop1)
    
        # tutup file
        text_file.close()
        tfilename = self.strNow + "_create_" + self.lowerTableName + "_table.php"
        out_file_name = os.path.join(self.dir_path, self.working_dir, 'database', 'migrations', tfilename )
        out_file = open(out_file_name, 'w')
        out_file.writelines(data_file)
        
        out_file.close()
    # END OF: def BuatFileMigrasi():

        

    # **********************************
    # Buat File Model
    # **********************************
    def BuatFileModel(self):            
        text_file_name = os.path.join(self.dir_path, 'b_model.php')    
        print('read: ', text_file_name)
        text_file = open(text_file_name, 'r')
        data_file = text_file.read()

        # ubah setiap variabel
        for lf in self.lfdict :
            # print(fdict[lf])
            data_file = data_file.replace(lf, self.fdict[lf])
    
        # ubah bagian yang di Loop1
        loop1 = ""
        for item in self.tableFields:
            loop1 += "        '" + item[1] + "', \n"
        
        data_file = data_file.replace('_Loop1_', loop1)
    
        # tutup file
        text_file.close()
        tfilename = self.tableName + ".php"
        out_file_name = os.path.join(self.dir_path, self.working_dir, 'app', 'Models', tfilename )
        out_file = open(out_file_name, 'w')
        out_file.writelines(data_file)
        
        out_file.close()
    
    # END OF: def ():
        
        
    
    # **********************************
    # Buat File Controller
    # **********************************
    def BuatFileController(self):            
        text_file_name = os.path.join(self.dir_path, 'b_controller.php')    
        print('read: ', text_file_name)
        text_file = open(text_file_name, 'r')
        data_file = text_file.read()

        # ubah setiap variabel
        for lf in self.lfdict :
            # print(fdict[lf])
            data_file = data_file.replace(lf, self.fdict[lf])
    
        # ubah bagian yang di Loop1
        loop1 = ""
        for item in self.tableFields:
            loop1 += "			'" + item[1] + "' \t\t=> $request->" + item[1] + ", \n"
        
        data_file = data_file.replace('_Loop1_', loop1)
    
        # tutup file
        text_file.close()
        tfilename = self.tableName + "Controller.php"
        out_file_name = os.path.join(self.dir_path, self.working_dir, 'app', 'Http', 'Controllers', tfilename )
        out_file = open(out_file_name, 'w')
        out_file.writelines(data_file)
        
        out_file.close()
    
    # END OF: def ():
        
    
        
    # **********************************
    # Buat File View Index
    # **********************************
    def BuatFileViewIndex(self):            
        text_file_name = os.path.join(self.dir_path, 'bv_index.blade.php')    
        print('read: ', text_file_name)
        text_file = open(text_file_name, 'r')
        data_file = text_file.read()

        # ubah setiap variabel
        for lf in self.lfdict :
            # print(fdict[lf])
            data_file = data_file.replace(lf, self.fdict[lf])
    
        # ubah bagian yang di Loop1
        loop1 = ""
        for item in self.tableFields:
            loop1 += "                                    <th>" + item[1].upper() + "</th> \n"
        
        data_file = data_file.replace('_Loop1_', loop1)
        
        # ubah bagian yang di Loop2
        loop2 = ""
        for item in self.tableFields:
            loop2 += "                                        <td>{{ $" + self.tablenameVar + "->" + item[1] + " }}</td>\n"
        
        data_file = data_file.replace('_Loop2_', loop2)        
    
        # tutup file
        text_file.close()
        tfilename = "index.blade.php"
        out_file_name = os.path.join(self.dir_path, self.working_dir,'resources', 'views', self.tableName, tfilename )
        out_file = open(out_file_name, 'w')
        out_file.writelines(data_file)
        
        out_file.close()
    
    # END OF: def ():    
    
        
    # **********************************
    # Buat File View Show
    # **********************************
    def BuatFileViewShow(self):            
        text_file_name = os.path.join(self.dir_path, 'bv_show.blade.php')    
        print('read: ', text_file_name)
        text_file = open(text_file_name, 'r')
        data_file = text_file.read()

        # ubah setiap variabel
        for lf in self.lfdict :
            # print(fdict[lf])
            data_file = data_file.replace(lf, self.fdict[lf])
    
        # ubah bagian yang di Loop1
        loop1 = ""
        for item in self.tableFields:
            loop1 += "                            <dt>" + item[1].upper() +\
                "</dt><dd>{{ $" + self.tablenameVar + "->" + item[1] + " }}</dd> \n"
        
        data_file = data_file.replace('_Loop1_', loop1)
        
        
        # tutup file
        text_file.close()
        tfilename = "show.blade.php"
        out_file_name = os.path.join(self.dir_path, self.working_dir,'resources', 'views', self.tableName, tfilename )
        out_file = open(out_file_name, 'w')
        out_file.writelines(data_file)
        
        out_file.close()
    
    # END OF: def ():    
    
    
    # **********************************
    # Buat File View Create
    # **********************************
    def BuatFileViewCreate(self):            
        text_file_name = os.path.join(self.dir_path, 'bv_create.blade.php')    
        print('read: ', text_file_name)
        text_file = open(text_file_name, 'r')
        data_file = text_file.read()

        # ubah setiap variabel
        for lf in self.lfdict :
            # print(fdict[lf])
            data_file = data_file.replace(lf, self.fdict[lf])
    
        # ubah bagian yang di Loop1
        isiLoopOri = """
                            <div class="form-group mb-3">
                                <label class="font-weight-bold">_itemU_</label>
                                <input type="text" class="form-control @error('_item_') is-invalid @enderror" name="_item_" value="{{ old('_item_') }}" placeholder="...">
                            
                                <!-- error message untuk _item_ -->
                                @error('_item_')
                                    <div class="alert alert-danger mt-2">
                                        {{ $message }}
                                    </div>
                                @enderror
                            </div>
        """
        loop1 = ""
        for item in self.tableFields:
            isiLoop = isiLoopOri.replace('_itemU_', item[1].upper())
            isiLoop = isiLoop.replace('_item_', item[1])
            loop1 += isiLoop
        
        data_file = data_file.replace('_Loop1_', loop1)
                
    
        # tutup file
        text_file.close()
        tfilename = "create.blade.php"
        out_file_name = os.path.join(self.dir_path, self.working_dir,'resources', 'views', self.tableName, tfilename )
        out_file = open(out_file_name, 'w')
        out_file.writelines(data_file)
        
        out_file.close()
    
    # END OF: def ():    
        
    
    # **********************************
    # Buat File View Edit
    # **********************************
    def BuatFileViewEdit(self):            
        text_file_name = os.path.join(self.dir_path, 'bv_edit.blade.php')    
        print('read: ', text_file_name)
        text_file = open(text_file_name, 'r')
        data_file = text_file.read()

        # ubah setiap variabel
        for lf in self.lfdict :
            # print(fdict[lf])
            data_file = data_file.replace(lf, self.fdict[lf])
    
        # ubah bagian yang di Loop1
        isiLoopOri = """
                            <div class="form-group mb-3">
                                <label class="font-weight-bold">_itemU_</label>
                                <input type="text" class="form-control @error('_item_') is-invalid @enderror" name="_item_"  value="{{ old('_item_', $_tablenameVar_->_item_) }}"  placeholder="...">
                            
                                <!-- error message untuk _item_ -->
                                @error('_item_')
                                    <div class="alert alert-danger mt-2">
                                        {{ $message }}
                                    </div>
                                @enderror
                            </div>
        """
        loop1 = ""
        for item in self.tableFields:
            isiLoop = isiLoopOri.replace('_itemU_', item[1].upper())
            isiLoop = isiLoop.replace('_item_', item[1])
            isiLoop = isiLoop.replace('_tablenameVar_', self.tablenameVar)            
            loop1 += isiLoop
        
        data_file = data_file.replace('_Loop1_', loop1)
                
    
        # tutup file
        text_file.close()
        tfilename = "edit.blade.php"
        out_file_name = os.path.join(self.dir_path, self.working_dir,'resources', 'views', self.tableName, tfilename )
        out_file = open(out_file_name, 'w')
        out_file.writelines(data_file)
        
        out_file.close()
    
    # END OF: def ():    


 # --- END of: CLASS



# ======================================
# MAIN FUNCTION
# ======================================
gen = MyLaravelGenerator()

print('buat file migrasi')
gen.BuatFileMigrasi()

print('')
print('buat file model')
gen.BuatFileModel()

print('')
print('buat file controller')
gen.BuatFileController()

print('')
print('buat file View Index')
gen.BuatFileViewIndex()

print('')
print('buat file View Show')
gen.BuatFileViewShow()

print('')
print('buat file View Create')
gen.BuatFileViewCreate()

print('')
print('buat file View Edit')
gen.BuatFileViewEdit()