$.fn.dataTableExt.oPagination.input = {
    "fnInit": function (oSettings, nPaging, fnCallbackDraw)
    {
    	var nFirst = $('<a class="paginate_button first" href="#"><i class="icon-double-angle-left"></i></a>');
        var nPrevious = $('<a class="paginate_button previous" href="#"><i class="icon-angle-left"></i></a>');
        var nNext = $('<a class="paginate_button next" href="#"><i class="icon-angle-right"></i></a>');
        var nLast = $('<a class="paginate_button last" href="#"><i class="icon-double-angle-right"></i></a>');
        var nInput = $('<input type="text" style="width:30px; display:inline; text-align:center;" />');
        //var nPage = $('<span class="paginate_page">Страница</span>')
        //var nOf = $('<span class="paginate_of"></span>')

        if (oSettings.sTableId !== ''){
            $(nPaging).attr('id', oSettings.sTableId+'_paginate');
            nPrevious.attr('id', oSettings.sTableId+'_previous');
            nNext.attr('id', oSettings.sTableId+'_next');
            nLast.attr('id', oSettings.sTableId+'_last');
        }
          
        $(nPaging).append(nFirst);
        $(nPaging).append(nPrevious);
        //$(nPaging).append(nPage);
        $(nPaging).append(nInput);
        //$(nPaging).append(nOf);
        $(nPaging).append(nNext);
        $(nPaging).append(nLast);
          
        nFirst.click( function () {
            oSettings.oApi._fnPageChange(oSettings, "first");
            fnCallbackDraw(oSettings);
        });
          
        nPrevious.click(function() {
            oSettings.oApi._fnPageChange(oSettings, "previous");
            fnCallbackDraw(oSettings);
        });
          
        nNext.click( function() {
            oSettings.oApi._fnPageChange(oSettings, "next");
            fnCallbackDraw(oSettings);
        });
          
        nLast.click( function() {
            oSettings.oApi._fnPageChange(oSettings, "last");
            fnCallbackDraw( oSettings );
        });
          
        nInput.keyup( function(e) {
            if (e.which == 38 || e.which == 39){
                this.value++;
            } else if ((e.which == 37 || e.which == 40) && this.value > 1){
                this.value--;
            }
              
            if (this.value == "" || this.value.match(/[^0-9]/)){
                /* Nothing entered or non-numeric character */
                return;
            }
              
            var iNewStart = oSettings._iDisplayLength * (this.value - 1);
            if (iNewStart > oSettings.fnRecordsDisplay()){
                /* Display overrun */
                oSettings._iDisplayStart = (Math.ceil((oSettings.fnRecordsDisplay()-1) /
                    oSettings._iDisplayLength)-1) * oSettings._iDisplayLength;
                fnCallbackDraw(oSettings);
                return;
            }
              
            oSettings._iDisplayStart = iNewStart;
            fnCallbackDraw(oSettings);
        });
          
        /* Take the brutal approach to cancelling text selection */
        $('span', nPaging).bind( 'mousedown', function () { return false; } );
        $('span', nPaging).bind( 'selectstart', function () { return false; } );
    },
     
     
    "fnUpdate": function (oSettings, fnCallbackDraw)
    {
        if (!oSettings.aanFeatures.p)
        {
            return;
        }
        var iPages = Math.ceil((oSettings.fnRecordsDisplay()) / oSettings._iDisplayLength);
        var iCurrentPage = Math.ceil(oSettings._iDisplayStart / oSettings._iDisplayLength) + 1;
        
        if (iCurrentPage == 1){
        	$('.paginate_button.first').add('.paginate_button.previous').addClass('disabled');
        } else{
        	$('.paginate_button.first').add('.paginate_button.previous').removeClass('disabled');
        }
        
        if (iCurrentPage == iPages){
        	$('.paginate_button.last').add('.paginate_button.next').addClass('disabled');
        } else {
        	$('.paginate_button.last').add('.paginate_button.next').removeClass('disabled');
        }
        
        /* Loop over each instance of the pager */
        var an = oSettings.aanFeatures.p;
        for (var i=0, iLen=an.length ; i<iLen ; i++){
            //var spans = an[i].getElementsByTagName('span');
            var inputs = an[i].getElementsByTagName('input');
            //spans[1].innerHTML = " из "+iPages
            inputs[0].value = iCurrentPage;
        }
    }
};