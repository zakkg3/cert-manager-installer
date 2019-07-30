# cert-manager-installer

An alternative, automated and easy way to install cert-manager using Helmfile


## Helmfile

Helmfile is a declarative spec for deploying helm charts.

## Requirements:

 * kubectl
 * Helm
 * helmfile (https://github.com/roboll/helmfile).
 
## Steps:
 
1.- Clone this repo:

    git clone git@github.com:zakkg3/cert-manager-installer.git
    cd cert-manager-installer
    
3.- Run:

    helmfile sync


Helmfile will process all the the helm charts defined inside `helmfile.d` directory in alphabetical order. (install crd's then annotate the namespace and finally install cert-manager chart)


### Troubleshooting

Please read [Troubleshooting installation](https://docs.cert-manager.io/en/latest/getting-started/troubleshooting.html)

#### Disable webhook

Include the following lines in  helmfile.d/01-cert-manager.yaml

        values:
          - webhook:
              enabled: false
