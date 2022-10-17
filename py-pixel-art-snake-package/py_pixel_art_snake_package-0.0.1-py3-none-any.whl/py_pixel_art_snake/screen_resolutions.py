
import os
import pytest
import pygame
import pygame_gui

from tests.shared_fixtures import _init_pygame, default_ui_manager, default_display_surface, \
    _display_surface_return_none
from tests.shared_comparators import compare_surfaces

from pygame_gui.ui_manager import UIManager
from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu
from pygame_gui.core.ui_container import UIContainer





try:
    # mouse button constants not defined in pygame 1.9.3
    pygame.BUTTON_LEFT
    pygame.BUTTON_MIDDLE
    pygame.BUTTON_RIGHT
except AttributeError:
    pygame.BUTTON_LEFT = 1
    pygame.BUTTON_MIDDLE = 2
    pygame.BUTTON_RIGHT = 3


def test_select_option_from_drop_down(self, _init_pygame, default_ui_manager,
                                          _display_surface_return_none):
        test_container = UIContainer(relative_rect=pygame.Rect(0, 0, 300, 300),
                                     manager=default_ui_manager)
        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(10, 10, 200, 30),
                              manager=default_ui_manager,
                              container=test_container)

        menu.current_state.should_transition = True
        menu.update(0.01)

        assert menu.selected_option == 'eggs'
        flour_button = menu.current_state.options_selection_list.item_list_container.elements[1]

        flour_button.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,
                                                      {'button': pygame.BUTTON_LEFT,
                                                       'pos': flour_button.rect.center}))

        flour_button.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP,
                                                      {'button': pygame.BUTTON_LEFT,
                                                       'pos': flour_button.rect.center}))

        for event in pygame.event.get():
            default_ui_manager.process_events(event)

        for event in pygame.event.get():
            default_ui_manager.process_events(event)

        assert menu.selected_option == 'flour'