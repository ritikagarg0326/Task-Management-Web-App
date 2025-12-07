# Step 1: Use Node image
FROM node:18

# Step 2: Create app directory
WORKDIR /app

# Step 3: Copy package.json & package-lock.json
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install -g @angular/cli
RUN npm install

# Step 5: Copy project files
COPY . .

# Step 6: Expose Angular dev server port
EXPOSE 4200

# Step 7: Run Angular in development mode
CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]
