from PySide6.QtWidgets import QMenu

from miranda.framework.components.controls.dockers.menubar.menubar_item import MenuItem

# Contains an arrow on it's side to show that it contains submenus
class Menu(QMenu):
    def __init__(self, title = None, parent = None):
        super().__init__(title = title, parent = parent)

    # menuitems
    # type: Menu
    def addMenuItems(self, *menus):
        for menu in menus:
           self.__determine_menutype_add_action(menu)
            
    def addMenuItem(self, menu):
        self.__determine_menutype_add_action(menu)
        
    # To avoid redundancy in addMenuItem and addMenuItems, this functions shall handle all logic
    def __determine_menutype_add_action(self, menu):
        if isinstance(menu, Menu):
            self.addAction(menu.menuAction())
        elif isinstance(menu, MenuItem):
            self.addAction(menu)
            
    """
    Build menu from JSON template structure
    """
    def fromTemplate(self, template):
        menus = self.create_menu(template)
        
        for menu in menus:
            self.addAction(menu)
        # self.addItem(menus)
            
    # This method isn't working
    def create_menu(self, menu_structure):
        items = []
        for item in menu_structure:
            if "type" in item and item["type"] == "separator":
                menu_item = MenuItem("Hey")
                # menu_item.setSeparator(True)
                items.append(menu_item)
            else:
                menu_item = MenuItem(item["label"])
                if "submenu" in item:
                    submenu_items = self.create_menu(item["submenu"])
                    for submenu_item in submenu_items:
                        # items.push(submenu_item)
                        continue
                else:
                    continue
                    if "click" in item:
                        menu_item.click = item["click"]
                    if "accelerator" in item:
                        menu_item.accelerator = item["accelerator"]
                    if "role" in item:
                        menu_item.role = item["role"]
                items.append(menu_item)
                
        # print(items)
        return items
