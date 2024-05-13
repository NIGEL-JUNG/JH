// 이 부분은 필요한 경우에만 추가하세요.
// 예를 들어, 버튼 클릭 시 알림창을 띄우는 기능을 추가하고 싶다면 아래와 같이 작성할 수 있습니다.
document.addEventListener("DOMContentLoaded", function() {
    const welcomeButton = document.getElementById("welcome-button");
    welcomeButton.addEventListener("click", function() {
        alert("환영합니다!");
    });
});
