// @flow

import { combineReducers } from 'redux';

import preflights from 'plans/reducer';
import products from 'products/reducer';
import user from 'accounts/reducer';

import type { PreflightsState } from 'plans/reducer';
import type { Products } from 'products/reducer';
import type { User } from 'accounts/reducer';

export type AppState = {
  +user: User,
  +products: Products,
  +preflights: PreflightsState,
};

const reducer = combineReducers({
  user,
  products,
  preflights,
});

export default reducer;
