<?php

/*
 * DataTables example server-side processing script.
 *
 * Please note that this script is intentionally extremely simply to show how
 * server-side processing can be implemented, and probably shouldn't be used as
 * the basis for a large complex system. It is suitable for simple use cases as
 * for learning.
 *
 * See http://datatables.net/usage/server-side for full details on the server-
 * side processing requirements of DataTables.
 *
 * @license MIT - http://datatables.net/license_mit
 */

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Easy set variables
 */

function pg_connection_string_from_database_url() {
extract(parse_url($_ENV["DATABASE_URL"]));
return "user=$user pass=$pass host=$host db=" . substr($path, 1); # <- you may want to add sslmode=require there too
}

// DB table to use
$table = 'scrapedresults';

// Table's primary key
$primaryKey = 'id';

// Array of database columns which should be read and sent back to DataTables.
// The `db` parameter represents the column name in the database, while the `dt`
// parameter represents the DataTables column identifier. In this case simple
// indexes
$columns = array(
	array( 'db' => 'term', 'dt' => 0 ),
	array( 'db' => 'location',  'dt' => 1 ),
	array( 'db' => 'jobposition',   'dt' => 2 ),
	array( 'db' => 'department',     'dt' => 3 ),
	array( 'db' => 'agency',     'dt' => 4 ),
	array( 'db' => 'dateposted',     'dt' => 5 ),
	array( 'db' => 'link',     'dt' => 6 )
);

// SQL server connection information
$sql_details = array(pg_connection_string_from_database_url
);


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * If you just want to use the basic configuration for DataTables with PHP
 * server-side, there is no need to edit below this line.
 */

require( 'ssp.class.php' );

echo "here i am!!!!!!!!!!!!!!"
echo json_encode(
	SSP::simple( $_GET, $sql_details, $table, $primaryKey, $columns )
);


