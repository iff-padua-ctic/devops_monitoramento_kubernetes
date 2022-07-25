# Dashboards com Grafana e Prometheus

https://www.youtube.com/watch?v=fzny5uUaAeY&t=5s <br>
https://docs.technotim.live/posts/kube-grafana-prometheus/ <br>



1 - Adicionando o repositório do Prometheus no helm <br>
    $ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts <br>
    $ helm repo update  <br>

1.1 Criar o namespace no kubernetes <br>
    $ kubectl create namespace monitoring <br>

1.2 Definir o usuário e senha <br>
    $ echo -n 'seu_usuario' > ./admin-user # mude o usuário <br>
    $ echo -n 'sua_senha' > ./admin-password # mude a senha <br>

1.3 Criando o secret <br>
    $ kubectl create secret generic grafana-admin-credentials --from-file=./admin-user --from-file=admin-password -n monitoring <br>

    $ kubectl describe secret -n monitoring grafana-admin-credentials <br>

    $ kubectl get secret -n monitoring grafana-admin-credentials -o jsonpath="{.data.admin-user}" | base64 --decode <br>

    $ kubectl get secret -n monitoring grafana-admin-credentials -o jsonpath="{.data.admin-password}" | base64 --decode <br>

    #removendo os arquivos
    $ rm admin-user && rm admin-password


2 - Instalação do Prometheus e Graphana <br>
    <a href="https://github.com/techno-tim/launchpad/tree/master/kubernetes/kube-prometheus-stack">Download do values do Prometheus</a> <br>

    #Execute para Instalação
    $ helm install -n monitoring prometheus prometheus-community/kube-prometheus-stack -f values.yaml    <br>

    #Execute para atualização/modificação do values
    $ helm upgrade -n monitoring prometheus prometheus-community/kube-prometheus-stack -f values.yaml    <br>

    #Desinstalar  <br>
    #https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack <br>
    $ helm uninstall -n monitoring prometheus prometheus-community/kube-prometheus-stack   <br>


    $ kubectl delete crd alertmanagerconfigs.monitoring.coreos.com  <br>
    $ kubectl delete crd alertmanagers.monitoring.coreos.com  <br>
    $ kubectl delete crd podmonitors.monitoring.coreos.com  <br>
    $ kubectl delete crd probes.monitoring.coreos.com  <br>
    $ kubectl delete crd prometheuses.monitoring.coreos.com  <br>
    $ kubectl delete crd prometheusrules.monitoring.coreos.com  <br>
    $ kubectl delete crd servicemonitors.monitoring.coreos.com  <br>
    $ kubectl delete crd thanosrulers.monitoring.coreos.com  <br>





3 - Acesso <br>
    #Mapera porta local  <br>
    $ kubectl port-forward -n monitoring   pod/grafana-848b5fdff-hvrkb  52222:80   <br>
    
    http://<IP_CLUSTER>:52222     <br>


4 - Exemplos <br>
    https://github.com/techno-tim/launchpad/tree/master/kubernetes/kube-prometheus-stack <br>

    https://github.com/techno-tim/launchpad <br>











