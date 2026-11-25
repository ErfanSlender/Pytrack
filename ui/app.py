import customtkinter as ctk


        # Theme Settings

ctk.set_appearance_mode('dark')

ctk.set_default_color_theme('dark-blue')

class PyTrackApp(ctk.CTk):
    
    
    def __init__(self):
        super().__init__()
        
        # Window Settings
        self.title('PyTrack')
        self.geometry('1100*700')
        self.minsize(900, 600)
        
        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color='#181820'
        )
        
        self.sidebar.pack(
            side='left',
            fill='y'
        )
        
        self.sidebar.pack_propagate(False)
        
        # Logo
        self.logo = ctk.CTkLabel(
            self.sidebar,
            text='PyTrack',
            font=('Arial', 28, 'bold'),
            text_color='#3B82F6'
        )
        self.logo.pack(pady=35)
        
        # Navigation Buttons
        self.dashboard_btn = ctk.CTkButton(
            self.sidebar,
            text='Dashboard',
            height=45,
            corner_radius=10,
            command=lambda:
                self.show_page('Dashboard')
        )
        
        self.dashboard_btn.pack(
            padx=15,
            pady=10,
            fill='x'
        )
        
        self.transactions_btn = ctk.CTkButton(
            self.sidebar,
            text='Transactions',
            height=45,
            corner_radius=10,
            command=lambda:
                self.show_page('Transactions')
        )
        
        self.transactions_btn.pack(
            padx=15,
            pady=10,
            fill='x'
        )
        
        self.report_btn = ctk.CTkButton(
            self.sidebar,
            text='Reports',
            height=45,
            corner_radius=10,
            command=lambda:
                self.show_page('Reports')
        )
        
        self.report_btn.pack(
            padx=15,
            pady=10,
            fill='x'
        )
        
        # Main Content
        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color='#101014'
        )
        
        self.main_frame.pack(
            side='right',
            fill='both',
            expand=True
        )
        
        # Page Title
        self.page_title = ctk.CTkLabel(
            self.main_frame,
            text='Dashboard',
            font=('Arial', 30, 'bold')
        )
        
        self.page_title.pack(
            anchor='w',
            padx=35,
            pady=35
        )
        
        # Main Title
        self.title_label = ctk.CTkLabel(
            self,
            text='PyTrack',
            font=('Arial', 32, 'bold')
        )

        self.title_label.pack(pady=40)
        
                # Background
        self.configure(fg_color='#101014')
    # Change Page
    def show_page(self, page_name):
        self.page_title.configure(
            text=page_name
        )
    
if __name__ == '__main__':
    app = PyTrackApp()
    app.mainloop()