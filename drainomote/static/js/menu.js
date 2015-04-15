( function( $ ) {
 /*** 
  * Run this code when the #toggle-menu link has been tapped
  * or clicked
  */
 $( '#toggle-menu' ).on( 'touchstart click', function(e) {
  e.preventDefault();

  var $body = $( 'body' ),
      $main = $( '#main' ),
      $menu = $( '#menu' ),
 
      /* Cross browser support for CSS "transition end" event */
      transitionEnd = 'transitionend webkitTransitionEnd otransitionend MSTransitionEnd';

 $body.addClass( 'animating' );

  /* When the toggle menu link is clicked, animation starts */
if ( $body.hasClass( 'show-menu' ) ) {
   $body.removeClass( 'show-menu' );
  } else {
  $body.addClass( 'show-menu' );
}

  /***
   * When the animation (technically a CSS transition)
   * has finished, remove all animating classes and
   * either add or remove the "menu-visible" class 
   * depending whether it was visible or not previously.
   */
  $menu.on( transitionEnd, function() {
   $body
    .removeClass( 'animating' )

   $menu.off( transitionEnd );
  } );
 } );
} )( jQuery );