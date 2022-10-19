class Styles(object):
    def __init__(self):

        self.text_combo_list_style = '''
            QListView {
                background: #656565;
                border: 1px solid gray;
                color: white;
                border-radius: 0px;
            }
        
            QListView::item {
                border: None;
                background: transparent;
                margin:3px;
                height: 24px;
            }                             
        
            QListView::item:selected { 
                border: None;
                margin:3px;
                color: white;
                background: #232323; 
                height: 24px;
            }
        
            QListView::item:selected:!active {
                background: #323232;
                border: None;
            }
        
            QListView::item:selected:active {
                background: #323232;
                border: None;
            }
        
            QListView::item:hover {
                background: #323232;
                border: None;
            }
        '''

        self.text_combo_style = '''
            /*---------------------- QComboBox -----------------------*/
            QComboBox {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                selection-background-color: transparent;
                color: white;
                background-color: transparent;
                border: None;
                border-radius: 5px;
                padding: 0px 0px 0px 5px;
                margin: 0px;
            }
            
            QComboBox:item {
                background: #323232;
                color: white;
                min-height: 10px;
                margin: 0px;
            }
            
            QComboBox:item:selected
            {
                border: None;
                background: #232323;
                margin: 0px;
            }
            
            
            QComboBox:editable {
                background: transparent;
            }
            
            QComboBox:!editable, QComboBox::drop-down:editable {
                 background: #656565;
            }
            
            /* QComboBox gets the "on" state when the popup is open */
            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                background: transparent;
            }
            
            QComboBox:on { /* shift the text when the popup opens */
                padding: 3px;
                color: white;
                background-color: transparent;
                selection-background-color: transparent;
            }
            
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-top: None;
                border-bottom: None;
                border-left-width: 1px;
                border-left-color: transparent;
                border-left-style: solid; /* just a single line */
                border-top-right-radius: 3px; /* same radius as the QComboBox */
                border-bottom-right-radius: 3px;
            }
            
            QComboBox::down-arrow {
                image: url(icons/tdown.svg);
                width: 13px;
                height: 14px;
                padding-right: 3px;
            }
            
            QComboBox::down-arrow:on { /* shift the arrow when popup is open */
                top: 1px;
                left: 1px;
            }
            
            QComboBox QAbstractItemView {
                border: 2px solid darkgray;
            }
            
            QComboBox QListView {
                background: #656565;
                border: 1px solid gray;
                color: white;
                border-radius: 0px;
            }
        
            QComboBox QListView::item {
                border: None;
                background: transparent;
                margin:3px;
                height: 24px;
            }                             
        
            QComboBox QListView::item:selected { 
                border: None;
                margin:3px;
                color: white;
                background: #232323; 
                height: 24px;
            }
        
            QComboBox QListView::item:selected:!active {
                background: #323232;
                border: None;
            }
        
            QComboBox QListView::item:selected:active {
                background: #323232;
                border: None;
            }
        
            QComboBox QListView::item:hover {
                background: #323232;
                border: None;
            }

        '''
