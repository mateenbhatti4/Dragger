$(document).ready(function()
{
    $('[data-toggle="tooltip"]').tooltip();

    // $('#heading').draggable({
    //     revert: "invalid",
    //     stack: "#heading",
    //     helper: 'clone'
    // });
    // $('#drop').droppable({
    //     accept: "#heading",
    // drop: function (event, ui) {
    //     var droppable = $(this);
    //     var draggable = ui.draggable;
    //     // Move draggable into droppable
    //     draggable.clone().appendTo(droppable);
    //     //draggable.css({top: '5px', left: '5px'});
    // }
    // });
    // $( "#selectable" ).selectable();
    // $("body").on('click',"#column1",function (){
    //     // alert("Hello");
    //     $('.col4').remove();
    //     $('.col2').remove();
    //     $('.col3').remove();
    //     $('.otl').remove();
    //     $('.otr').remove();
    //     $('.karo').append('<div class="col-sm-12 borders col1">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n');
    // });
    // $("body").on('click',"#column2",function (){
    //     // alert("Hello");
    //     $('.col1').remove();
    //     $('.col4').remove();
    //     $('.col3').remove();
    //     $('.otl').remove();
    //     $('.otr').remove();
    //     $('.karo').append('<div class="col-sm-6 borders col2">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div>\n' +
    //         '            <div class="col-sm-6 borders col2">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n');
    // });
    // $("body").on('click',"#column3",function (){
    //     // alert("Hello");
    //     $('.col1').remove();
    //     $('.col2').remove();
    //     $('.col4').remove();
    //     $('.otl').remove();
    //     $('.otr').remove();
    //     $('.karo').append('<div class="col-sm-4 borders col3">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div>\n' +
    //         '            <div class="col-sm-4 borders col3">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div>\n' +
    //         '            <div class="col-sm-4 borders col3">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div><br>');
    // });
    // $("body").on('click',"#column4",function (){
    //     // alert("Hello");
    //     $('.col1').remove();
    //     $('.col2').remove();
    //     $('.col3').remove();
    //     $('.otl').remove();
    //     $('.otr').remove();
    //     $('.karo').append('<div class="col-sm-3 borders col4">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div>\n' +
    //         '            <div class="col-sm-3 borders col4">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div>\n' +
    //         '            <div class="col-sm-3 borders col4">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div><br>' +
    //         '            <div class="col-sm-3 borders col4">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div><br>');
    // });
    // $("body").on('click',"#onethird-right",function (){
    //     // alert("Hello");
    //     $('.col1').remove();
    //     $('.col2').remove();
    //     $('.col3').remove();
    //     $('.col4').remove();
    //     $('.otl').remove();
    //     $('.karo').append('<div class="col-sm-8 borders otr">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div>\n' +
    //         '            <div class="col-sm-4 borders otr">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n');
    // });
    // $("body").on('click',"#onethird-left",function (){
    //     // alert("Hello");
    //     $('.col1').remove();
    //     $('.col2').remove();
    //     $('.col3').remove();
    //     $('.col4').remove();
    //     $('.otr').remove();
    //     $('.karo').append('<div class="col-sm-4 borders otl">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n' +
    //         '            </div>\n' +
    //         '            <div class="col-sm-8 borders otl">\n' +
    //         '                <div style="border-bottom: 2px solid #a7a3a3; text-align: center" class="add">\n' +
    //         '                    <button style="text-align:center;outline: none; border: none; background: #a7a3a3; border-radius: 50%; position: relative; top: 12px" data-toggle="modal" data-target="#draggingMenu">\n' +
    //         '                        <i class=\'bx bx-plus\'></i>\n' +
    //         '                    </button>\n' +
    //         '                </div>\n');
    // });
    // $( "#draggable" ).draggable({ revert: true, helper: "clone" });
    // $( "#droppable" ).droppable({
    //   drop: function( event, ui ) {
    //     $( this )
    //       .addClass( "ui-state-highlight" )
    //       .find( "p" )
    //         .html( "Dropped!" );
    //   }
    // });

//     $('#draggable').draggable({
//     revert: "invalid",
//     stack: ".draggable",
//     helper: 'clone'
// });
// $('#droppable').droppable({
//     accept: "#draggable",
//     drop: function (event, ui) {
//         var droppable = $(this);
//         console.log(droppable)
//         var draggable = ui.draggable;
//         console.log(draggable)
//         // Move draggable into droppable
//         draggable.clone().appendTo(droppable).addClass( "ui-state-highlight" )
//           .find( "p" )
//             .html( "Dropped!" );
//         //draggable.css({top: '5px', left: '5px'});
//     }
// });
});


