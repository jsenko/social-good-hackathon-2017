import React, { Component } from 'react';
//import { List, fromJS, Range } from 'immutable';
//import './sudoku.css';

const JSON = {
	name: "Mgr. Jaroslav Topol",
	ic: {
		attr:"IC:",
		value: 71346414
	},
	ec: {
		attr:"EC:",	
		value: 13198
	},
	state: {
		attr: "Stav:",
		value: "Aktivni"
	},
	residence: {
		attr:"Sidlo:",
		value: `Na Zlatnici 301/2
		Praha 4, 147 00`

	},		
	email: {
		attr: "E-mail:",
		value: "info@ak-topol.cz"
	},
	stats: {
		rulingsCount: {
			attr: "pocet rozhodnuti",
			value: 542
		},
		topCategory: {
			attr: "top kategorie",
			value: "rodinne pravo"
		},
		succ: {
			attr: "meritorni konecne rozhodnuti",
			value: 344
		},
		fail: {
			attr: "nemeritorni konecne rozhodnuti",
			value: 186
		},
		stop: {
			attr: "rozhodnuti o zastaveni rizeni",
			value: 12
		},
		succRate: {
			attr: "uspesnost",
			value: 345
		}
	}
};

class Container extends Component {
	constructor() {
		super();
		this.state = {
			advocate: JSON
		};
	}

	render() {
		return (
			<div id="Container">
				<Header />
				<PersonalInfo person={this.state.advocate}/>
				<Statistics stats={this.state.advocate.stats}/>
			</div>
		);
	}
}

function Header() {
	return (
		<div id="Header">
			<nav id="mainNav"></nav>
			<div id="map"></div>
			<h1>CESTI ADVOKATI.CZ</h1>
		</div>
 	);
}

function PersonalInfo(props) {
	return (
		<div id="PersonalInfo">
			<h2 className="personName">{props.person.name}</h2>
			<Info attr={props.person.ic.attr} value={props.person.ic.value}/>
			<Info attr={props.person.ec.attr} value={props.person.ec.value}/>
			<Info attr={props.person.state.attr} value={props.person.state.value}/>
			<Info attr={props.person.residence.attr} value={props.person.residence.value}/>
			<Info attr={props.person.email.attr} value={props.person.email.value}/>
		</div>
	);
}

function Info(props) {
	return(
		<div className="Info">
				<span className="attr">{props.attr}</span><span className="value">{props.value}</span>	
		</div>
	);
}

class Statistics extends Component {
	constructor(){
		super();
		this.state = {
		};
	}

	render(){
		return (
			<div>STATS</div>
		);
	}
}

export default Container;
