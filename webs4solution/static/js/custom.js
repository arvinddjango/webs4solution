function toTitleCase(str) {
    return str.replace(/(?:^|\s)\w/g, function(match) {
        return match.toUpperCase();
    });
}
var url = location.href;
var array = url.split('/');
var lastsegment = toTitleCase(array[array.length-1].replace(/-/g," "));

if($("select#hire_select_service option[value='"+lastsegment+"']").length > 0){
	$("select#hire_select_service").val(lastsegment);
}