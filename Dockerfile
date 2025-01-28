FROM alpine:latest

WORKDIR /metacall

# intall curl and metacall
RUN apk add curl \
	&& curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh

COPY requirements.txt ./
COPY package.json package-lock.json ./

RUN metacall pip3 install -r requirements.txt \
    && metacall npm install

COPY . .

EXPOSE 8080

CMD ['metacall','index.js']



