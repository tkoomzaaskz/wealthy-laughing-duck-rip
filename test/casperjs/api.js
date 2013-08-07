var url = casper.cli.get('url');

casper.test.begin('API test', function suite(test) {

        casper.start(url, function() {
                test.assertTitle('Wealthy Laughing Duck API');
                test.assertExists('body');
        });

        casper.then(function() {
                test.assertExists('head');
        });

        casper.run(function() {
                test.done();
        });
});
