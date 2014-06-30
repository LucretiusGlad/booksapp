$(document).ready(function(){
	window.BooksAppView = AppView.extend({
		
		item_name: 'книгу',
		
		sAjaxSource: book_table_path,
		
		dataTablesDrawCallback: function() {
			$('.view_item_btn').add('.view_item').each(function(){
				var bookViewBtn = new BookViewBtn({el: this});
			});
			
			$('.remove_item_btn').each(function(){
				var bookRemoveBtn = new BookRemoveBtn({el: this});
			});

			$('.edit_item_btn').each(function(){
				var bookEditBtn = new BookEditBtn({el: this});
			});
		}
		
	
	})

	var booksAppView = new BooksAppView();
	
	window.BookCreateBtn = CreateBtn.extend({
		dialog_title: 'Создать книгу',
		
		form_path: book_form_path,
		
		itemTable: booksAppView.itemTable,
		
	})
	
	bookCreatBtn = new BookCreateBtn();
	
	window.BookViewBtn = ViewBtn.extend({
		dialog_title: 'Информация о книге',
		
		info_path: book_info_path
	})
	
	window.BookRemoveBtn = RemoveBtn.extend({
		remove_title: 'Удалиать книгу',
		
		remove_message: 'Вы уверены, что хотите удалить книгу ',
		
		remove_path: book_remove_path,
		
		remove_confirm_msg: 'Книга <%= title %> успешно удалена',
	})
	
	window.BookEditBtn = EditBtn.extend({
		edit_title: 'Редактировать книгу',
		
		edit_form_path: book_edit_form_path,
		
		edit_path: book_edit_path,
	})
	
})