# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:25:13 2023

@author: Jagrati Garg
"""

class Book:
    def __init__(self,authorlast,authorfirst,title,place,publisher,year):
        self.authorlast=authorlast
        self.authorfirst=authorfirst
        self.title=title
        self.place=place
        self.publisher=publisher
        self.year=year
    def write_bib_entry(self):
        return self.authorlast \
               + ', ' + self.authorfirst \
               + ', ' + self.title + ', ' + self.place \
               + ':  ' + self.publisher + ', ' \
               + self.year + '.'
  
beauty=Book("Dubay","Thomas","The Evidential Power of Beauty","San Francisco","Ignatius Press","1999")
pynut=Book("Martelli","Alex","Python in a Nutshell","Sebastopol, CA", "O'Reilly Media, Inc.", "2003")  
print(pynut.write_bib_entry()) 
print(beauty.write_bib_entry())
beauty.year="2021"
print(beauty.write_bib_entry())
