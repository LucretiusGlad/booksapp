$(document).ready(function(){
	window.AuthorsAppView = AppView.extend({
		
		item_name: 'автора',
		
		sAjaxSource: author_table_path,
		
		dataTablesDrawCallback: function() {
			$('.view_item_btn').add('.view_item').each(function(){
				var authorViewBtn = new AuthorViewBtn({el: this});
			});
			
			$('.remove_item_btn').each(function(){
				var authorRemoveBtn = new AuthorRemoveBtn({el: this});
			});

			$('.edit_item_btn').each(function(){
				var authorEditBtn = new AuthorEditBtn({el: this});
			});
		}
	})

	var authorsAppView = new AuthorsAppView();
	
	window.AuthorCreateBtn = CreateBtn.extend({
		dialog_title: 'Создать автора',		
		form_path: author_form_path,
	})
	
	authorCreatBtn = new AuthorCreateBtn();
	
	window.AuthorViewBtn = ViewBtn.extend({
		dialog_title: 'Информация об авторе',
		
		info_path: author_info_path
	})
	
	window.AuthorRemoveBtn = RemoveBtn.extend({
		remove_title: 'Удалиать автора',
		
		remove_message: 'Вы уверены, что хотите удалить автора ',
		
		remove_path: author_remove_path,
		
		remove_confirm_msg: 'Автор <%= title %> успешно удален',
	})
	
	window.AuthorEditBtn = EditBtn.extend({
		edit_title: 'Редактировать автора',
		
		edit_form_path: author_edit_form_path,
		
		edit_path: author_edit_path,
	})
	
})