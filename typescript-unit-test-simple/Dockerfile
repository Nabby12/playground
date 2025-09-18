FROM node:lts-slim

WORKDIR /app

COPY tsconfig.json jest.config.js ./
COPY package.json .
RUN npm install

COPY src/index.ts src/index_test.ts ./src/

CMD [ "npx", "jest", "--color" ]
