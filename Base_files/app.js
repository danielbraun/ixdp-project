$(document).ready(function() {
	$("input[name=week_day]").change(function(event) {
		$("circle[week-day-verbose=" + event.target.value + "]").toggle();
	});
	$("circle").attr('cy', function(index, attr) {
		return (600 - $(this).attr('cy'));
	});
});