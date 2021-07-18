FROM mcr.microsoft.com/powershell

LABEL MAINTAINER="TTL_0"

#RUN RUN apt-get update && apt-get -y install wget
#RUN wget https://raw.githubusercontent.com/anthonyhendricksS2/MailSniper/master/MailSniper.ps1
ADD https://raw.githubusercontent.com/anthonyhendricksS2/MailSniper/master/MailSniper.ps1 /MailSniper.ps1

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/opt/microsoft/powershell/7/pwsh"]
CMD []