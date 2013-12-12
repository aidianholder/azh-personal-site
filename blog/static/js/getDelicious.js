$(document).ready(function(){
	
	$.getJSON("http://feeds.delicious.com/v2/json/aidianholder?count=3&callback=?",
		function(json) {
		$(json).each(function(index){
			/*$.each(this.t, function(i, tag){console.log(i, tag)});*/
			
			var nodeContent = '<a href="' + this.u + '">' + this.d + '</a>'
			/*if (this.n) {
				nodeContent += '<br/><p>' + this.n +'</p>'
			}*/
			/*if (this.t) {
				nodeContent += "<span>" 
				$.each(this.t, function(i, tag){nodeContent += '<a href="http://www.delicious.com/aidianholder/' + tag +'">' + tag + '</a> '})
			nodeContent += "</span>"
				}*/
			$('<li></li>').html(nodeContent) 
				.appendTo('#bookmarks');
			
			})
		}	
	)	
})
