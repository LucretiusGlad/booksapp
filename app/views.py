#-*-coding: utf-8 -*-
from flask import jsonify, request, session, render_template, redirect, url_for
from sqlalchemy import or_

from app import app

class BaseTableView(object):
    '''
    A base class for interaction with jquery.dataTables.js
    '''
    
    #SQLAlchemy model class. should be overriden by a child
    model = None
    
    #should be overriden by a child
    columns_map = {}
    
    def render_to_response(self):
        '''
        Returning a json-data for the jquery.dataTables.js
        '''
        context = self.get_context()
        return jsonify(**context)
    
    def get_context(self):
        '''
        Building data for returned json.
        '''
        s_echo = request.args.get('sEcho')
        item_list, total_records, total_display_records = self.get_item_list()
        aaData = [self.get_data(i) for i in item_list]
        
        context = {
            'sEcho': s_echo,
            'aaData': aaData, 
            'iTotalRecords': total_records,
            'iTotalDisplayRecords': total_display_records}
        return context
    
    def get_data(self, item):
        return {
            'DT_RowId': item.id,
            'DT_RowClass': '',
            '0': item.id,
            '1': self.get_edit_link(item),
            '2': self.get_action_links(item) 
        }
    
    def get_edit_link(self, item):
        '''
        Constructing an html for edit link of an item.
        '''
        link_str = u'<a class="view_item item_name" item_id="{0}" href="">{1}</a>'
        return link_str.format(item.id, item.name)
    
    def get_action_links(self, item):
        '''
        Constructing an html for action links of an item.
        '''
        context = {'item': item}
        return render_template('_action_btns.html', **context)
    
    def get_item_list(self):
        '''
        Getting a list of items to display.
        '''
        
        #Getting the data from GET request sent by dataTables
        display_start = int(request.args.get('iDisplayStart'))
        display_length = int(request.args.get('iDisplayLength'))
        search_param = request.args.get('sSearch') or None
        sort_col = request.args.get('iSortCol_0') or None
        sort_dir = request.args.get('sSortDir_0') or None
        
        session['num_display'] = display_length
        display_end = display_start + display_length
        queryset = self.get_queryset()
        
        #Getting filtered qs if search param is indicated.
        final_queryset = self.get_filtered_qs(search_param, queryset)
        
        #Getting sorted qs if sort_col param is indicated.
        final_queryset = self.get_sorted_qs(sort_col, sort_dir, final_queryset)
        
        #Slicing the queryset according to the selected page.
        qs_slice = final_queryset[display_start:display_end]
        queryset_count = queryset.count()
        final_queryset_count = final_queryset.count()
        return (qs_slice, queryset_count, final_queryset_count)
        
    def get_queryset(self):
        return self.model.query
    
    def get_filtered_qs(self, search_param, queryset):
        """
        Filtering the qs on item id, name.
        """
        #Filtering only if the search_param was indicated, otherwise returning
        #unfiltered qs.
        if not search_param:
            return queryset
        
        search_param = u'{0}{1}{0}'.format('%', search_param)
        
        params = [self.model.id.ilike(search_param),
                  self.model.name.ilike(search_param)]
        filter_list = queryset.filter(or_(*params))
        return filter_list
   
    def get_sorted_qs(self, sort_col, sort_dir, queryset):
        """
        Getting sorted qs according to the sorted col and sort direction.
        """
        if sort_col:
            param = self.get_sort_param(sort_col, sort_dir)
            return queryset.order_by(param)
        return queryset
    
    def get_sort_param(self, sort_col, sort_dir):
        '''
        Getting the param for order_by method.
        '''
        col_name = self.columns_map.get(sort_col)
        param = getattr(self.model, col_name)
        if sort_dir == 'desc':
            param = getattr(param, 'desc')
            return param()
        return param

@app.route('/')
def home():
    return redirect(url_for('books.book_list'))
    
        