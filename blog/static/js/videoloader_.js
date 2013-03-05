$(document).ready(function(){
			var viewport;
			$(".show").colorbox({width:function(){
				viewport = $("#main").width();
				if (viewport > 600) {width = "482"}
				else if ((viewport < 600) && (viewport >= 480)) {width = "322"}
				else {width = "242"}
				return width;
				}
				});
			
})