provider "kubernetes" {
  config_path = "~/.kube/config"
}

data "kubernetes_service" "python_web_app_service" {
  metadata {
    name = "python-web-app-service"
    namespace = "demo"
  }
}

output "service_info" {
  value = {
    name      = data.kubernetes_service.python_web_app_service.metadata[0].name
    namespace = data.kubernetes_service.python_web_app_service.metadata[0].namespace
    cluster_ip = data.kubernetes_service.python_web_app_service.spec[0].cluster_ip
    port      = data.kubernetes_service.python_web_app_service.spec[0].port[0].port
  }
  #output_file = "service_info.json"
}
resource "null_resource" "write_service_info" {
  provisioner "local-exec" {
    command = <<EOT
echo '{
  "name": "${data.kubernetes_service.python_web_app_service.metadata[0].name}",
  "namespace": "${data.kubernetes_service.python_web_app_service.metadata[0].namespace}",
  "cluster_ip": "${data.kubernetes_service.python_web_app_service.spec[0].cluster_ip}",
  "port": ${data.kubernetes_service.python_web_app_service.spec[0].port[0].port}
}' > service_info.json
EOT
  }
}