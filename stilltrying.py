self.Left = ttk.Frame(self, width=300, height=1000, relief="raise")
        self.Left.pack(side=LEFT)
        self.btn_show = ttk.Button(self.Left, text="LOAD", command=Read)
        self.btn_show.pack(side=TOP)
        self.btn_back = ttk.Button(self.Left, text="ADD", command=open_insert_record)
        self.btn_back.pack(side=RIGHT)
        self.Right = ttk.Frame(self, width=600, height=500, relief="raise")
        self.Right.place(x=150, y=45)
        # ==================================LIST WIDGET========================================
        # ==================================LIST WIDGET========================================


        global tree

        scrollbary = Scrollbar(self.Right, orient=VERTICAL)
        scrollbarx = Scrollbar(self.Right, orient=HORIZONTAL)
        tree = ttk.Treeview(self.Right, columns=(
        "st_id", "st_name", "c_name", "c_code", "f_name", "quizes", "midterm", "finals", "total"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('st_id', text="ID", anchor=W)
        tree.heading('st_name', text="Name", anchor=W)
        tree.heading('c_name', text="Course Name", anchor=W)
        tree.heading('c_code', text="Course Code", anchor=W)
        tree.heading('f_name', text="Faculty Name", anchor=W)
        tree.heading('quizes', text="Quizes", anchor=W)
        tree.heading('midterm', text="Midterm", anchor=W)
        tree.heading('finals', text="Fianls", anchor=W)
        tree.heading('total', text="Total Marks", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=120)
        tree.column('#2', stretch=NO, minwidth=0, width=120)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=120)
        tree.column('#5', stretch=NO, minwidth=0, width=120)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.column('#8', stretch=NO, minwidth=0, width=120)
        tree.pack()

        self.lbl = Label(self, text="ADD A NEW BOOK RECORD", font=(("Helvetica", "16")))
        self.lbl.place(x=100, y=20)
        global ACCESSION
        global ENTRYDATE
        global TITLE
        global PUBLISHER
        global EDITOR
        global SUBTITLE
        global PRICE
        global VENDOR
        # ==========variables#==================
        ACCESSION = StringVar()
        ENTRYDATE = StringVar()
        TITLE = StringVar()
        PUBLISHER = StringVar()
        EDITOR = StringVar()
        SUBTITLE = StringVar()
        PRICE = StringVar()
        VENDOR = StringVar()
        self.lbl_Accession_number = Label(self, text="Accession No", font=("Helvetica", 16)).place(x=30, y=50)
        self.lbl_Entry_data = Label(self, text="Entry Date", font=("Helvetica", 16)).place(x=30, y=100)
        self.lbl_Title = Label(self, text="Title", font=("Helvetica", 16)).place(x=30, y=150)
        self.lbl_Publisher = Label(self, text="Publisher", font=("Helvetica", 16)).place(x=30, y=200)
        self.lbl_Editor = Label(self, text="Editor", font=("Helvetica", 16)).place(x=30, y=250)
        self.lbl_Subtitle = Label(self, text="Sub-Title", font=("Helvetica", 16)).place(x=30, y=300)
        self.lbl_Price = Label(self, text="Price", font=("Helvetica", 16)).place(x=30, y=350)
        self.lbl_Vendor = Label(self, text="Vendor", font=("Helvetica", 16)).place(x=30, y=400)

        # ===================Entry===================================#
        self.ent_Accession_number = Entry(textvariable=ACCESSION).place(x=200, y=55)
        self.ent_Entry_data = Entry(textvariable=ENTRYDATE).place(x=200, y=110)
        self.ent_Title = Entry(textvariable=TITLE).place(x=200, y=150)
        self.ent_Publisher = Entry(textvariable=PUBLISHER).place(x=200, y=200)
        self.ent_Editor = Entry(textvariable=EDITOR).place(x=200, y=250)
        self.ent_Subtitle = Entry(textvariable=SUBTITLE).place(x=200, y=300)
        self.ent_Price = Entry(textvariable=PRICE).place(x=200, y=350)
        self.ent_Vendor = Entry(textvariable=VENDOR).place(x=200, y=400)
        self.btn_add = Button(text="Add+", font=("Helvetica", 16), command=add_book).place(x=350, y=450)
        self.lbl_add = Label(text="Complete", fg="red").place(x=250, y=450)
        self.btn_back_home = Button(text="BACK", font=("Helvetica", 16)).place(x=450, y=450)

        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)