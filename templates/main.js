
// 使用純 JavaScript 實作生成隨機 token 的函式
function generateRandomToken(length = 32) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let token = '';
    for (let i = 0; i < length; i++) {
      // 從 characters 中隨機選取一個字符
      token += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return token;
  }
  
  // 生成一個 32 字元長度的 token
  let token = generateRandomToken(32);
  
  // 計算 30分鐘的過期時間（單位：毫秒）
  let expireTime = Date.now() + 30 * 60 * 1000;
  
  let XsendBtn = document.querySelector('#submitbtn1999');
  
  function debounce(func, delay) {
    let timer;
    return function(...args) {
      if (timer) return; // 如果計時器已經存在，直接返回，不執行函數
      timer = setTimeout(() => {
        timer = null; // 延遲時間到後清除計時器
      }, delay);
      func.apply(this, args);
    };
  }
  
  
  let userIP = ""; // 全域變數儲存 IP
  
  // 先取得 IP
  fetch("https://api64.ipify.org?format=json")
      .then(response => response.json())
      .then(data => {
          userIP = data.ip; // 存入全域變數
          console.log("使用者 IP:", userIP);
      })
      .catch(error => {
          console.error("取得 IP 失敗:", error);
          userIP = "UNKNOWN"; // 如果失敗則設置為 UNKNOWN
      });
  
  
  
      function cleanName(name) {
      return name.replace(/[.,!?@#%^&*(){}[\]\\/'"<>:;+=~`$|]/g, "").trim();
  }
  
  function isValidEmail(email) {
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
  }
  
  async function send() {
      let name = document.getElementsByName("name")[0].value.trim();
      let email = document.getElementsByName("email")[0].value.trim();
  
      // **清理 Name**
      let cleanedName = cleanName(name);
  
      // **檢查是否輸入**
      if (!cleanedName || !email) {
          alert("❌ 請輸入姓名和 Email！");
          return;
      }
  
      // **檢查 Email 格式**
      if (!isValidEmail(email)) {
          alert("❌ Email 格式錯誤，請輸入有效的 Email！");
          return;
      }
  
      // **檢查 LocalStorage 是否有重複提交**
      let lastSubmission = localStorage.getItem("lastSubmission");
      if (lastSubmission) {
          let lastData = JSON.parse(lastSubmission);
          if (lastData.name === cleanedName || lastData.email === email) {
              alert("⚠️請勿重複提交資料！");
              return;
          }
      }
  
      // **儲存這次輸入的資料到 LocalStorage**
      localStorage.setItem("lastSubmission", JSON.stringify({ name: cleanedName, email }));
  
      // **顯示 alert，不影響 AJAX 執行**
      alert("✅ 提交成功！幾分鐘後記得在垃圾信件中檢查看看唷~");
  
      // **按鈕狀態變更**
      let submitBtn = document.querySelector("#submitbtn1999 > a");
      submitBtn.innerHTML = "發送中...";
      submitBtn.style.pointerEvents = "none"; // 防止連續點擊
  
      window.location.href = "https://www.instagram.com/booxing_1999/";
    const apiKey = "{{ sheet_api }}";
      // **非同步發送 AJAX**
      try {
          let response = await $.ajax({
              url: apiKey,
              type: "POST",
              data: {
                  "name": cleanedName,
                  "email": email,
                  "token": token,
                  "expireTime": expireTime,
                  "userIP": userIP
              }
          });
  
          console.log("✅ 資料已提交，後端回應:", response);
  
          if (response === "資料提交成功") {
  
                  window.location.href = "https://www.instagram.com/booxing_1999/";
  
          } else {
              console.error("⚠️ 伺服器回應異常:", response);
              alert("❌ 提交失敗，請稍後再試！");
          }
      } catch (error) {
          console.error("❌ 提交錯誤:", error);
          alert("❌ 伺服器發生錯誤，請稍後再試！");
      } finally {
          // **恢復按鈕狀態**
          submitBtn.innerHTML = "提交";
          submitBtn.style.pointerEvents = "auto";
      }
  
      // **清空輸入欄位**
      document.getElementsByName("name")[0].value = "";
      document.getElementsByName("email")[0].value = "";
  }
  
  
  // 使用防抖函數來包裝 send 函數，設定 3 秒冷卻時間
  XsendBtn.addEventListener('click', debounce(send, 500));
  
  
  
  
  function adjustMargin() {
      var element = document.querySelector(".containerInner.ui-sortable");
      if (window.innerWidth < 768) {
          element.style.marginTop = "-150px";
      } else {
          element.style.marginTop = "";  // 電腦版恢復原狀
      }
  
      
  }
  
  // **當頁面載入時執行**
  adjustMargin();
  
  // **當視窗大小變化時執行**
  window.addEventListener("resize", adjustMargin);