# alwaysnote

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### Add redirection rules for s3
```
<RoutingRules>

  <RoutingRule>

    <Condition>

      <HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals>

    </Condition>

    <Redirect>

      <Protocol>https</Protocol>

      <HostName>[YOUR_DOMIAN]</HostName>

      <ReplaceKeyPrefixWith>#!/</ReplaceKeyPrefixWith>

    </Redirect>

  </RoutingRule>

</RoutingRules>
```