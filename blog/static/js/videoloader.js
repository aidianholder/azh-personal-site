$(document).ready(function(){
			var viewport;
			$(".thumbnail").colorbox({width:function(){
				viewport = $("#main").width();
				if (viewport > 600) {width = "490"}
				else if ((viewport < 600) && (viewport >= 480)) {width = "332"}
				else {width = "242"}
				return width;
				}
				});
			
})