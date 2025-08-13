const refresh = () => {
    window.location.reload()
    console.log("refreshed");
}
const logout = () => {
    const logoutForm = document.getElementById("logoutForm")
    logoutForm.submit()
}
