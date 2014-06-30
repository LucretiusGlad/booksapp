$(document).ready(function(){
	window.AppView = Backbone.View.extend({
		el: 'body',
		
		dt_base_options: {
			"aaSorting": [[ 0, "desc" ]],
			"oLanguage": {
				"sInfo": "Просмотр записей с _START_ по _END_ из _TOTAL_",
				"sInfoFiltered": "всего записей _MAX_",
				"sLengthMenu": "Показывать _MENU_ записей",
				"sProcessing": "Загрузка...",
				"sSearch": "Поиск:",
				"sInfoThousands": " ",
				"sZeroRecords": "Данные отсутствуют"
		    },
		    //"bScrollInfinite": true,
		    //"bScrollCollapse": true,
		    //"sScrollY": "300px",
		    "bAutoWidth": false,
			"sPaginationType": "input",
			"bProcessing": true,
			"bServerSide": true,	
			"iDisplayLength": 10,
			"aoColumns": [null, null, { "bSortable": false }],
		    
			"sAjaxSource": null,
			"fnDrawCallback": null
		},
		
		sAjaxSource: null, //should be overriden by children
		
		initialize: function() {
			this.initDataTables();
			this.addCreateBtn();
		},
		
		initDataTables: function() {
			//Initialize dataTables
			this.update_options();
			window.itemTable = $('.list_table').dataTable(this.dt_base_options);
		},
		
		update_options: function() {
			$.extend(this.dt_base_options, 
					{"fnDrawCallback": this.dataTablesDrawCallback,
					 "sAjaxSource": this.sAjaxSource})
		},
		
		dataTablesDrawCallback: null, //should be overriden by children
		
		addCreateBtn: function() {
			var btn = $('<button class="btn btn-primary add_btn">' + 
                       '<i class="icon-plus bigger-130"></i>' + 
                       'Добавить ' + this.item_name +
                       '</button>')
            $('#DataTables_Table_0_wrapper .span6:eq(1)').append(btn);
		}
	})
	
	window.CreateBtn = Backbone.View.extend({
		el: '.add_btn',
		
		events: {'click': 'openAddDialog'},
		
		dialog: null,
		
		openAddDialog: function() {
			var self = this;
			var dialog = bootbox.dialog({
				title: this.dialog_title,
				message: this.get_add_form(),
				className: 'form_dialog',
				buttons: {
					success: {
						label: 'Создать',
						className: 'btn-success',
						callback: function() {
							self.createItem();
							return false;
						}
					},
					cancel: {
						label: 'Отменить'
					}
				}
			})
			this.dialog = dialog;
		},
		
		get_add_form: function() {
			var returnVal;
			var self = this;
			$.ajax({
				url: self.form_path,
				type: 'get',
				async: false,
				success: function(data) {
					returnVal = data;
				} 
			});
			return returnVal;
		},
		
		createItem: function() {
			var self = this;
			$('.item_form').ajaxSubmit({
				success: function(responseText, statusText, xhr, $form) {
					self.processResponse(responseText, self.dialog);
				}
			});
		},
		
		processResponse: function(data, dialog) {
			if(data.status == 'success'){
				dialog.modal('hide');
				window.itemTable.fnDraw();
			} else {
				dialog.find('.bootbox-body').html(data.form_html);
			}
		}
	})
	
	window.ViewBtn = Backbone.View.extend({
		events: {'click': 'openViewDialog'},
		
		dialog_title: null, //should be overriden by a child
		
		openViewDialog: function(e) {
			var btn = $(e.target);
			var item_id = btn.attr('item_id'); 
			bootbox.dialog({
				title: this.dialog_title,
				message: this.get_info(item_id),
				className: 'form_dialog',
				buttons: {
					cancel: {
						label: 'ОК'
					}
				}
			})
			return false;
		},
		
		get_info: function(item_id) {
			var self = this;
			var returnVal;
			$.ajax({
				url: self.info_path,
				data: {item_id:item_id},
				type: 'get',
				async: false,
				success: function(data) {
					returnVal = data;
				}
			});
			return returnVal;
		}
	}) 
	
	window.RemoveBtn = Backbone.View.extend({
		events: {'click': 'removeItem'},
		
		removeItem: function(e) {
			var self = this;
			var btn = $(e.target);
			var item_id = btn.attr('item_id')
			bootbox.dialog({
				title: this.remove_title,
				message: this.remove_message + this.get_name(item_id) + "?",
				className: 'form_dialog',
				buttons: {
					success: {
						label: 'Удалить',
						className: 'btn-success',
						callback: function() {
							self.doRemoveItem(item_id);
						}					
					},
					cancel: {
						label: 'Отменить'
					}
				}
				
			})
		},
		
		get_name: function(item_id) {
			return '"' +  $('.item_name[item_id="' + item_id +'"]').html() + '"';
		},
		
		doRemoveItem: function(item_id) {
			var self = this;
			$.ajax({
				url: self.remove_path,
				data: {item_id:item_id},
				type: 'post',
				async: false,
				success: function(data) {
					var compiled = _.template(self.remove_confirm_msg);
					var dialog = bootbox.alert(compiled({title: self.get_name(item_id)}))
					window.itemTable.fnDraw();
					setTimeout(function(){
						dialog.modal('hide');
					}, 2000)
					
				}
			});
		}
	})
	
	window.EditBtn = Backbone.View.extend({
		events: {'click': 'editItem'},
		
		dialog: null,
		
		editItem: function(e) {
			var self = this;
			var btn = $(e.target);
			var item_id = btn.attr('item_id')
			var dialog = bootbox.dialog({
				title: this.edit_title,
				message: this.get_edit_form(item_id),
				className: 'form_dialog',
				buttons: {
					success: {
						label: 'Сохранить',
						className: 'btn-success',
						callback: function() {
							self.doEditItem(item_id);
							return false;
						}					
					},
					cancel: {
						label: 'Отменить'
					}
				}
			})
			this.dialog = dialog;
		},
		
		get_edit_form: function(item_id) {
			var returnVal;
			var self = this;
			$.ajax({
				url: self.edit_form_path,
				data: {item_id:item_id},
				type: 'get',
				async: false,
				success: function(data) {
					returnVal = data;
				} 
			});
			return returnVal;
		},	

		doEditItem: function(item_id) {
			var self = this;
			$('.item_form').ajaxSubmit({
				success: function(responseText, statusText, xhr, $form) {
					self.processResponse(responseText, self.dialog);
				}
			});
		},
		
		processResponse: function(data, dialog) {
			if(data.status == 'success'){
				dialog.modal('hide');
				window.itemTable.fnDraw();
			} else {
				dialog.find('.bootbox-body').html(data.form_html);
			}
		}
		
	})
	
})