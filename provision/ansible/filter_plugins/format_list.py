#!/usr/bin/env python

def format_list(list_, pattern):
    if list_:
      return [pattern % s for s in list_]
    else:
      return ""


class FilterModule(object):
    def filters(self):
        return {
            'format_list': format_list,
        }