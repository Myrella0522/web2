function confirmLogout(){
  const confirmar = confirm("Você realmente deseja sair da sua conta?");
  if(confirmar){
    window.location.href ='/logout';
  }else{
    return;
  }
}
