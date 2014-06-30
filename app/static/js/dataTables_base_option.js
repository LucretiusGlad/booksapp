var dt_base_options = {
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
	"iDisplayLength": 20,
	
	"aoColumns": [null, null, { "bSortable": false }],
    "sAjaxSource": null //should be overriden by a child
}