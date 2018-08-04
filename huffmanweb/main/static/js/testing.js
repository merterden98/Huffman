
$(document).ready(function(){

    $('a[href*="#"]').on('click', function (e) {
        e.preventDefault();
    
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 500, 'linear');
    });

    var peepee = $('#Layer1').drawsvg({duration: 1000,});
    peepee.drawsvg('animate');

    $('#kappa').css('opacity', 0);
    
    $('#introsvg').css('opacity',0);
    $('#introtext').css('opacity', 0);
    $('#information').css('opacity', 0);
    $('#Entropy').css('opacity', 0);
    $('#prefixsvg').css('opacity', 0);
    $('#prefix').css('opacity', 0);
    $('#optimalitysvg').css('opacity', 0);
    $('#optimality').css('opacity', 0);

    $('#huffmanalgosvg').css('opacity', 0);
    $('#huffmanalgo').css('opacity', 0);
    

    $('#foundsvg').css('opacity', 0);
    $('#found').css('opacity', 0);

    $('#blockingsvg').css('opacity', 0);
    $('#blocking').css('opacity', 0);

    $('#hilowsvg').css('opacity', 0);
    $('#hilow').css('opacity', 0);

    $('#succsvg').css('opacity',0);
    $('#succ').css('opacity',0);

    $('#addrec').css('opacity',0);
    $('#addrecsvg').css('opacity',0);

    $('#minmaxsvg').css('opacity',0);
    $('#minmax').css('opacity',0);

    $('#opansvg').css('opacity',0);
    $('#opan').css('opacity',0);


    $('#xfastsvg').css('opacity',0);
    $('#xfast').css('opacity',0);

    $('#opxsvg').css('opacity',0);
    $('#opx').css('opacity',0);

    $('#yfastsvg').css('opacity',0);
    $('#yfast').css('opacity',0);

    $('#amortsvg').css('opacity',0);
    $('#amort').css('opacity',0);

    $('#concsvg').css('opacity',0);
    $('#conc').css('opacity',0);






    $('#Intro').waypoint(function(){

      console.log('Here');
      $('#introsvg').css('opacity',1);

      var intro = $('#introsvg').drawsvg({duration: 5000,});
      $('#introtext').addClass('fadeIn');
      intro.drawsvg('animate');

    }), { offset: '-100'
    };

    $('#introtext').waypoint(function(){


        $('#information').css('opacity',1);
  
        var info = $('#information').drawsvg({duration: 5000,});
        $('#Entropy').addClass('fadeIn');
        info.drawsvg('animate');
  
      }), { offset: '75%'
      };


    $('#prefixsvg').waypoint(function(){


        $('#prefixsvg').css('opacity',1);
  
        var info = $('#prefixsvg').drawsvg({duration: 5000,});
        $('#prefix').addClass('fadeIn');
        info.drawsvg('animate');
  
      }), { offset: 'bottom-in-view'
      };



  $('#optimalitysvg').waypoint(function(){

    $('#optimalitysvg').css('opacity',1);

    var info = $('#optimalitysvg').drawsvg({duration: 5000,});
    $('#optimality').addClass('fadeIn');
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#huffmanalgosvg').waypoint(function(){

    $('#huffmanalgosvg').css('opacity',1);

    var info = $('#huffmanalgosvg').drawsvg({duration: 10000,});
    $('#huffmanalgo').addClass('fadeIn');
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#foundsvg').waypoint(function(){

    $('#foundsvg').css('opacity',1);

    var info = $('#foundsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#found').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom in view'
  };

  $('#blockingsvg').waypoint(function(){

    $('#blockingsvg').css('opacity',1);

    var info = $('#blockingsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#blocking').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#hilowsvg').waypoint(function(){

    $('#hilowsvg').css('opacity',1);

    var info = $('#hilowsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#hilow').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#succsvg').waypoint(function(){

    $('#succsvg').css('opacity',1);

    var info = $('#succsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#succ').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#addrecsvg').waypoint(function(){

    $('#addrecsvg').css('opacity',1);

    var info = $('#addrecsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#addrec').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#minmaxsvg').waypoint(function(){

    $('#minmaxsvg').css('opacity',1);

    var info = $('#minmaxsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#minmax').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };


  $('#opansvg').waypoint(function(){

    $('#opansvg').css('opacity',1);

    var info = $('#opansvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#opan').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#xfastsvg').waypoint(function(){

    $('#xfastsvg').css('opacity',1);

    var info = $('#xfastsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#xfast').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#opxsvg').waypoint(function(){

    $('#opxsvg').css('opacity',1);

    var info = $('#opxsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#opx').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#yfastsvg').waypoint(function(){

    $('#yfastsvg').css('opacity',1);

    var info = $('#yfastsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#yfast').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };


  $('#amortsvg').waypoint(function(){

    $('#amortsvg').css('opacity',1);

    var info = $('#amortsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#amort').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };

  $('#concsvg').waypoint(function(){

    $('#concsvg').css('opacity',1);

    var info = $('#concsvg').drawsvg({duration: 20000,});
    setTimeout(function (){
        $('#conc').addClass('fadeIn')}, 5000);
    info.drawsvg('animate');

  }), { offset: 'bottom-in-view'
  };







});


  $('#kappa').waypoint(function(direction) {
      
      if(direction == 'up'){

        $('#kappa').addClass('fadeIn');
        $('#kappa').removeClass('fadeOut');
      }


    }, { offset: '-15%'
    });





var huff = $('#huffman').drawsvg({duration: 5000,});
huff.drawsvg('animate');









