$(".img-wrap").hover(function(){
    $(this).children(".title").animate({height: '0px'}, 'easeInBounce');

    
  },
  function(){
    $(this).children(".title").animate({ height: '25%'}, 'easeOutBounce');
    }
  );