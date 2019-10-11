/* eslint-disable no-undef */

/* eslint-disable no-useless-return */

document.getElementById('textarea').focus()
const msgerForm = document.getElementById('food-form')
// const msgerInput = document.getElementById('textarea')
const msgerChat = document.getElementById('msger-chat')

var flag = document.getElementById('flag').value;
var PERSON_NAME = 'User'
var pname = "User";
const PERSON_IMG = '/../static/sent2.jpeg'
// const BOT_IMG = "{{ url_for('static', filename='bg.jpeg') }}"
const BOT_IMG = '/../static/bg.jpeg'
const BOT_NAME = 'Mobile Guru'

var NAME = false
var qry = false
// var fg = 1;
document.getElementById('fg').value = 1;
var word = "";

var end = 0;
msgerForm.addEventListener('submit', event => {
  event.preventDefault()
  event.stopImmediatePropagation()
  const msgerInput = document.getElementById('textarea')
  const msgText = msgerInput.value

  if (!msgText) return

  else {
    var out = appendMessage(PERSON_NAME, PERSON_IMG, 'right', msgText)
    if (NAME === false) {
      // var flag = document.getElementById('flag').value;
      document.getElementById('flag').value = 1
      var check = isName(out)
      if (check) {
        var pname = document.getElementById('pname');
        document.getElementById('pname').value = out;
        PERSON_NAME = out
        NAME = true
        document.getElementById('flag').value = 2
      }
    }
    else if (qry === false) {
      // while (msgText !== 'end') {

      //   // msgText = 'end';
      // }
      var msgg = msgText.toLowerCase().split(" ");
      for(i=0;i<msgg.length;i++) {
        // alert(msgg[i])
        if( msgg[i] == 'end' || msgg[i] == 'no' || msgg[i] == 'nothing' || msgg[i] == 'nothing.') {
          end = 1;
          document.getElementById('flag').value = 3;
        }
      }
      if (end == 1) {
        qry = true
      $.post('result', {
          text: word
      },
      function (data) {
          if (data != "()") {
            if (data == "No such phones Exist") {

              appendMessageBot2(src,BOT_NAME,BOT_IMG, 'left', data)
              document.getElementById('flag').value = 5;
            }
            if (data == "Couldn't understand you...") {

              appendMessageBot2(src,BOT_NAME,BOT_IMG, 'left', data)
              document.getElementById('flag').value = 5;
            }
            data = data.replace("[","");
            data = data.replace("]","");
            phones = data.split(",");
            
              // usr.focus()JSON.parse("[" + string + "]");
              // alert(data);
            var len = (phones.length-1)/2;
            if (len>=5) {
              len =5;
            }
            // if (len == 1) {

            // }
            for(i=0;i<len;i++) {
              var res = '';
              var src = '';
              res = res + phones[2*i].replace("'","")
              src = src + phones[2*i+1].replace("'","")
              appendMessageBot2(src,BOT_NAME,BOT_IMG, 'left', res)
            }
            // alert("thaa");
            // var fg = document.getElementById('fg').value;
            
            document.getElementById('fg').value = 1;
            // end = 0;
            
           
            
          }
      })
      }
      
      else {
        
        
        var keyword = ['cost','budget','price','rating','ram','memory','internal','storage','display','screen','camera','battery','processor','chipset'];
        // var msgg = msgText.toLowerCase().split(" ");
        for (i=0;i<(keyword.length); i++) {
          for (j=0;j<(msgg.length); j++) {
            if (keyword[i] == msgg[j]) {
              document.getElementById("fg").value = 0;
              // fg = 0;
              // alert("th");
            }

          }
        }
        // for(i in keyword) {
        //   if (i in msgText) {
        //      fg = 0;
        //   }
        //   else {
        //     fg = 1;
        //   }
        // }
        // if (fg==1) {
        //   // appendMessageBot(BOT_NAME,BOT_IMG, 'left', res)
        //   // alert("improper sentence given...");
        // }
        // else 
        var flag = document.getElementById('flag').value;
        var fg = document.getElementById('fg').value;
        if(fg==0 && flag != 3) {
          // alert("333")
          if (msgText[msgText.length - 1] === '.') {
            word += msgText.replace('.', ' . ') ;
          }
          else {
            word += msgText + ' . ' ;
          }
          // var flag = document.getElementById('flag').value;
          document.getElementById('flag').value = 4;
        }
        
      }
    }
    // alert(flag);
    // else if (qry === true) {
      
    // }
    msgerInput.value = ''
    botResponse()
  }
})


// eslint-disable-next-line camelcase
function isName (name) {
  var output = $.ajax({
    type: 'POST',
    url: '/api/check_name',
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify({ 'name': name }),
    async: false,
    function (response) {
      console.log(response)
    }
  }).responseText
  if (output) {
    var out = parseInt(output)
    return out
  }
}

function appendMessage (name, img, side, text) {
//   Simple solution for small apps
  const msgHTML = `
    
    <div class="msg ${side}-msg">
    <div class="msg-img" style="background-image: url(${img})"></div>

    <div class="msg-bubble">
        <div class="msg-info">
        <div class="msg-info-name">${name}</div>
        <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
    </div>
    </div>
`

  var data = $.ajax({
    url: '/change_name',
    data: JSON.stringify({
      'text': text
    }),
    type: 'POST',
    contentType: 'application/json;charset=UTF-8',
    async: false,
    function (response) {
      console.log(response)
    }
  }).responseText
  var res = JSON.parse(data)
  var response = res['name']
  msgerChat.insertAdjacentHTML('beforeend', msgHTML)
  msgerChat.scrollTop += 1000
  window.scrollBy(0, 1000)
  console.log(response)
  return (response)
}

function appendMessageBot (name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
    <div class="msg ${side}-msg">
    <div class="msg-img" style="background-image: url(${img})"></div>

    <div class="msg-bubble">
        <div class="msg-info">
        <div class="msg-info-name">${name}</div>
        <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
    </div>
    </div>
`
  msgerChat.insertAdjacentHTML('beforeend', msgHTML)
  msgerChat.scrollTop += 1000
  window.scrollBy(0, 1000)
}

function appendMessageBot2 (srcl,name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
    <div class="msg ${side}-msg">
    <div class="msg-img" style="background-image: url(${img})"></div>

    <div class="msg-bubble">
        <div class="msg-info">
        <div class="msg-info-name">${name}</div>
        <div class="msg-info-time">${formatDate(new Date())}</div>
        
        </div>
        <a class="msg-text" href = "${srcl}">${text}</a>
    </div>
    </div>
`
  msgerChat.insertAdjacentHTML('beforeend', msgHTML)
  msgerChat.scrollTop += 1000
  window.scrollBy(0, 1000)
}

const BOT_MSGS = [
  "Ohh... I can't understand what you trying to say. Sorry!",
  "My developer didn't design me to understand that question",
  'Sorry if my answers are not relevant. :))',
  'I feel sleepy! :('
]
var pname = document.getElementById('pname');
pnam = pname.value;
const BOT_INTRO_MSGS = [
  "It's nice to meet you , how can I help you?",
  'Hi, how can I help you?',
  'I am glad, you chose me as your adventurous mobile phone guide, how can I help you?'
]


const BOT_END_MSGS = [
  'Thanks a lot for using me...',
  'Still confused ?, feel free to consult me again...',
  'Byee :)'
  // "It's nice to meet you " + PERSON_NAME + ', how can I help you?',
  // 'I am glad, you chose me as your adventurous mobile phone guide, how can I help you?'
]

const BOT_ERR_MSGS = [
  "Sorry I couldn't get you.",
  "Sorry, I am programmed to suggest smartphones only.",
  "Your request is beyond my power."
]

const BOT_CONT_MSGS = [
  'Anything else that you missed ?',
  'Any other preferences ?',
  'Any extra qualities your phone should have ?'
]

const BOT_NAME_MSGS = [
  "Sorry, I still didn't get your name", 
  'I think you forgot to tell me your name',
  'My name is Mobile Guru. What is yours?'
]// Icons made by Freepik from www.flaticon.com


function botResponse () {
  var flag = document.getElementById('flag').value;
  var fg = document.getElementById('fg').value;
  // alert(flag)
  if (flag == 0) {  
    const r = random(0, BOT_MSGS.length - 1)
    var msgText = BOT_MSGS[r]
  }

  if (flag == 1) {
    const r = random(0, BOT_NAME_MSGS.length - 1)
    var msgText = BOT_NAME_MSGS[r]
  }
  if (fg==0 && flag == 2) {
    const r = random(0, BOT_ERR_MSGS.length - 1)
    var msgText = BOT_ERR_MSGS[r]
  }
  if (fg==1 && flag == 2) {
    const r = random(0, BOT_INTRO_MSGS.length - 1)
    var msgText = BOT_INTRO_MSGS[r]
  }
  if (flag == 3) {
    // alert("dhf");
    const r = random(0, BOT_END_MSGS.length - 1)
    var msgText = BOT_END_MSGS[r]
     document.getElementById('flag').value = 0;
    document.getElementById('fg').value = 1;

  }
  if (fg==0 && flag == 4) {
    const r = random(0, BOT_CONT_MSGS.length - 1)
    var msgText = BOT_CONT_MSGS[r]
  }
  
  if (fg == 1 && flag == 4) {
    const r = random(0, BOT_ERR_MSGS.length - 1)
    var msgText = BOT_ERR_MSGS[r]
    // alert(flag)
  }
  // if (fg === 1 && flag === 2) {
  //   const r = random(0, BOT_ERR_MSGS.length - 1)
  //   var msgText = BOT_ERR_MSGS[r]
  //   alert(flag)
  // }
  const delay = msgText.split('').length * 10
  setTimeout(() => {
    appendMessageBot(BOT_NAME,BOT_IMG, 'left', msgText)
  }, delay)
}

// Utils
function formatDate (date) {
  const h = '0' + date.getHours()
  const m = '0' + date.getMinutes()

  return `${h.slice(-2)}:${m.slice(-2)}`
}

function random (min, max) {
  return Math.floor(Math.random() * (max - min) + min)
}
