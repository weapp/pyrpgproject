# -*- coding: utf-8 -*-
# Copyright 2006 Hugo Ruscitti <hugoruscitti@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Scribes; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA

from pygame.sprite import Sprite
import pygame
from library.stdmodules import module

class Fps (Sprite,module.Module):
    "Informa el rendimiento del programa mediante el indicador FPS (cuadros por segundo)"
    
    def __init__ (self, surface, clock):
        "Inicia el controlador de rendimiento"
        
        Sprite.__init__ (self)
        self.clock = clock
        self.font = pygame.font.Font (None, 16)
        self.surface=surface

    def update (self):
        "Obtiene el rendimiento del programa"
        
        fps = int (self.clock.get_fps ())
        self.image = self.font.render ('FPS: ' + str (fps), 1, (255, 255, 100))
        self.rect = self.image.get_rect ()
        self.rect.move_ip(10,10)
        
    def draw(self):
        self.surface.blit(self.image,self.rect)
