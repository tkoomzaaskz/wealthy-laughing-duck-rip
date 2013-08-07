var url = casper.cli.get('url');
var duck = require('./duck');

casper.test.begin('API test', function suite(test) {

        casper.start(url, function() {
                test.assertTitle(duck.name);
                test.assertExists('body');
                this.clickLabel('users', 'a');
        });

        casper.then(function() {
                test.assertTextExists('Execute list');
                var x = casper.evaluate(function(){
                        return $("a").length;
                });
                this.echo('There are ' + x + ' <a> elements', 'COMMENT');
        });

        casper.run(function() {
                test.done();
        });
});
