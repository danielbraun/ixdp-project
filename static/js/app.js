$(document).ready(function() {
	$("input[name=week_day]").change(function(event) {
		$("circle[week-day-verbose=" + event.target.value + "]").toggle();
	});
});